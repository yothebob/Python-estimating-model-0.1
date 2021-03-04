import installsim as sim
import automodel as model
import sys
import proposal_writer as pw

bid_sections = int(input('how many sections do you need bid? (2): '))
bid_lf = []
bid_lfprice = []

def menu(bid_sections = 1):
    print()
    print()
    select = input('run quote? (y/n) \n : ')
    
    if 'y' in select.lower():
        gen = int(input('how many gens do you want to run? : '))
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
            try:
                pw.write_proposal(bid_lf[0],bid_lfprice[0],bid_lf[1],bid_lfprice[1])
            except:
                print('something went wrong...')
                menu(bid_sections)
        else:
            menu(bid_sections)
    else:
        sys.exit()
        
menu(bid_sections)

