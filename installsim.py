import random
import sys
import numpy


#this has been altered to work in conjunction with another program


test_problems = []
print('Install sim loaded...')
file = open('problems.txt', 'r')
with file:
    for line in file:
        test_problems.append(int(line))
    file.close()
print('problem list: ' + str(test_problems))
gen_days = []
total_gens = []
lf_day = []

def menu():
    rerun = input('run simulation?(y/n) \n : ')
    if 'y'.lower() in rerun:
        gen = 50
        prob_rate = int(input('rate of problem?'))
        run_simulation(gen,prob_rate)
    else:
        sys.exit()



def get_adv(_num):
    #print(_num)
    return round(numpy.average(_num))
    



def run_simulation(_gen,_prob_rate,_maxlf,_minlf,_lf):
    print('new run: Generation ' + str(_gen))
    
    hour = 0
    day = 0
    problem = 0
    run_problem = 0
    total_problems = 0
    gen = _gen
    max_lf = _maxlf#int(input('Max LF rate? : '))
    min_lf = _minlf#int(input('min LF rate? : '))
    job_lf = _lf#int(input('job LF? : '))
    start_lf = _lf
    max_lf_per_day = random.randrange(min_lf,max_lf)
    max_install_rate = (max_lf_per_day/8)/6
    install_rate = 0
    problem_rate = _prob_rate
    while job_lf > 0:   
        for mins in range(6):
            if install_rate < max_install_rate and run_problem == 0:
                install_rate += (max_install_rate/6)
                
            if mins == 5:
                mins = 0
                hour += 1
                day += .125
                problem = random.randrange(_prob_rate)
                
            if run_problem > 0:
                run_problem -= 1
                
            job_lf -= install_rate
            if hour == 8:
                hour = 0
                print('Day : '+ str(day))
                print('tot problems: ' + str(total_problems))
                
                
            if problem == 1:
                total_problems += 1
                problem = 0
                run_problem = random.choice(test_problems)
                install_rate = 0
                
    gen_days.append(day)
    total_gens.append(gen)
    lf_day.append(start_lf/day)
    gen -= 1
    if gen != 0:
        run_simulation(gen,problem_rate,max_lf,min_lf,start_lf)
    else:
        adv_rate = 5
    return get_adv(lf_day), round(numpy.std(lf_day))
        #save = open('result.csv','w')
        #with save:
        #   save.write('gen ,' + str(total_gens) + '\n')
        #    save.write('days ,' + str(gen_days) + '\n')
        #    save.write('lf per day ,' + str(lf_day) + '\n')
        #    save.write('avg ,' + str(round(numpy.average(lf_day),3)) + '\n ')
        #    save.write('std dev ,' + str(round(numpy.std(lf_day),3)) + '\n ')
        #    save.close()
        #gen_days.clear()
        #total_gens.clear()
        #menu()

        
#menu()  
