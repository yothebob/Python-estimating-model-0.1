import installsim as sim
import automodel as model
import sys
import proposal_writer as pw

bid_sections = int(input('how many sections do you need bid? \n: '))
start_bid_sections = bid_sections
bid_lf = []
bid_lfprice = []

def menu(bid_sections = 1):
    print()
    print()
    gen = 25
    prob_rate = int(input('rate of problem?'))
    max_lf = int(input('max LF per hour install rate? : '))
    min_lf = int(input('min LF per hour install rate? : '))
    lf = int(input('Total job lf?'))
    install_rate,std_dev = sim.run_simulation(gen,prob_rate,max_lf,min_lf,lf)
    print(install_rate,std_dev)
    lf_cost = model.run_sim(install_rate,std_dev,lf)
    bid_sections -= 1
    bid_lf.append(lf)
    bid_lfprice.append(lf_cost)
    if bid_sections == 0:
        #try:
        pw.write_proposal(bid_lf,bid_lfprice)
        #except:
            #print('something went wrong...')
            #menu(bid_sections)
    else:
        menu(bid_sections)

        
menu(bid_sections)

