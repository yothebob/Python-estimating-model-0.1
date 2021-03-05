import math
import random
import numpy
import sys


#this has been altered to work in conjunction with another program


def cal_materials(_spacing,_corners,_lf,_panel_cost,_corner_cost):
    total = int((_corners * _corner_cost) + ((_lf / _spacing) * _panel_cost))
    return total

print('automodel loaded...')

def cal_engineering(_material):
    cogs = .0425
    engineering = _material * cogs
    if engineering < 3000:
        engineering = 3000
    drafting = engineering * 1.5
    return engineering,drafting



def cal_adv_engineering(_total):
    st = float(_total/5737.7)
    res = float(numpy.log10(st)/.05294)
    res = round((25 * (.905) ** (res)),2)
    result = _total * (res / 100)
    print(result)



def cal_manual_eng(_material):
    pick_engineering = input('type "m" for eng/draft manual entry, type "s" for standard model rates')
    if pick_engineering.lower() == "m":
        eng = int(input('how much for engineering?'))
        draft = int(input('how much for drafting?'))
        return eng,draft
    elif pick_engineering.lower() == "s":
        return cal_engineering(_material)
        


def cal_field(_lf,_rate):
    labor_cost = 34.68
    workers = 2
    return ((((_lf / _rate)*8) * labor_cost)* workers)



def cal_total(_lf,_field,_material,_engineering,project_type,_drafting):
    cogs_pre = 0
    indirect_pre = 0

    if project_type == 1:
        cogs_pre = .054
        indirect_pre = .8259
    elif project_type == 2:
        cogs_pre = .044
        indirect_pre = .7813
    elif project_type == 3:
        cogs_pre = .1680
        indirect_pre = .7451
    elif project_type == 4:
        cogs_pre = 1
        indirect_pre = .7432
    elif project_type == 5:
        cogs_pre = .11
        indirect_pre = .7432

    cogs_supplies = math.ceil(_material * cogs_pre)
    direct_burden = math.ceil(_field * .16)
    total_direct = math.ceil(_field + _material + cogs_supplies + _engineering + direct_burden + _drafting)
    indirect = math.ceil(total_direct * indirect_pre)
    total_expenses = total_direct + indirect
    profit = math.ceil(total_expenses * .176454)
    total = math.ceil(total_expenses + profit)
    print("Materials: " + str(_material))
    print("Labor: "+ str(_field))
    print("Engineering: " + str(_engineering))
    print("Drafting: " + str(_drafting))
    print("Direct: " + str(total_direct))
    print("Indirect: " + str(indirect))
    print("Expenses: " + str(total_expenses))
    print("profit: " + str(profit))
    print("Total: " + str(total))
    return total



def start():
    user = input("What do you want to do? \n type 'data' to run est simulation \n type 'end' to close program \n type 'quote' to make a quote \n type 'pricing' for price per panel \n : ")
    if user.lower() == "data":
        run_sim()
    elif user.lower() == "end":
        sys.exit()
    elif user.lower() == "quote":
        get_estimate()
    elif user.lower() == "pricing":
        print("""
        price per panel: \n picket = 126 for fascia, 113 for surface. 8 for corners
        glass = 268 for fascia, 256 surface , 8 for corners
        BaseShoe(ss top rail/clading) = 566 per 4' panel, 306 per corner
        series 500 rail = 456 per 4' panel (stanchion), 410 per 4' for halfen + angle bracket, corner += 50 """
        
              )
        print()
        print()
        start()
    else:
        print("Sorry, I did not understand. Please try again...")
        #start()



def get_estimate(_install_rate,_lf):
    print()
    print()
    
    lf = _lf#int(input(" Job LF? : "))
    corner = int(input("number of corners? : "))
    spacing = int(input("post spacing? : "))
    panel_cost = int(input("typ cost per panel : "))
    corner_cost = int(input("additional cost for corners? : "))
    engineering_cost = int(input('cost for drafting/engineering? : '))
    install_rate = _install_rate
    project_type = int(input("1-5 what type of project is it? refer to excel estimating model : "))

    print()
    print()
    
    material_cost = cal_materials(spacing,corner,lf,panel_cost,corner_cost)
    drafting_cost = 0
    labor_cost = cal_field(lf,int(_install_rate))
    total = cal_total(lf,labor_cost,material_cost,engineering_cost,project_type,drafting_cost)

    print("Job LF: " + str(lf))
    print("$/LF : " + str(round(total/lf)))
    print()
    print()
    
    #start()



def run_sim(_install_rate,_std_dev,_lf):

    #high_lf = int(input("max lf? \n : "))
    #low_lf = int(input("min LF? \n : "))
    #high_corners = math.ceil(high_lf / 100)
    #low_corners = 1
    lf = _lf
    spacing = int(input("What is the panel spacing? \n : "))
    panel_cost = int(input("What is typical cost per panel? \n : "))
    job_corners = int(input('how many corners? \n : '))
    corner_cost = int(input("What are additional costs needed for a corner? \n : "))
    engineering_cost = int(input('cost for drafting/engineering? : '))
    high_install_rate = _install_rate + _std_dev
    low_install_rate = _install_rate - _std_dev
    iterations = 25
    project_type = int(input("what project type? 1-5 \n: "))

    install_rates = []
    lfs = []
    corners = []
    totals = []
    per_lfs = []

    for gen in range(iterations):
        gen_lf = lf
        gen_corners = job_corners
        gen_install_rate = random.randrange(low_install_rate, high_install_rate)

        gen_materials = cal_materials(spacing,job_corners,lf,panel_cost,corner_cost)
        gen_engineering = engineering_cost
        gen_drafting = 0
        gen_field = cal_field(gen_lf,gen_install_rate)
        gen_total = cal_total(gen_lf,gen_field,gen_materials,gen_engineering,project_type,gen_drafting)
        print("Gen LF: " + str(gen_lf))
        print("Corners: " + str(gen_corners))
        print("LF/ day: " + str(gen_install_rate))
        print()
        print()
        install_rates.append(gen_install_rate)
        lfs.append(gen_lf)
        corners.append(gen_corners)
        totals.append(gen_total)
        per_lfs.append(round(gen_total/gen_lf))

    #file = open("estimates.csv","w")
    sim_avg_lf = numpy.average(per_lfs)
    sim_std_lf = numpy.std(per_lfs)
    sim_med_lf = numpy.median(per_lfs)
    print('-----------------------------------------------------')
    print("average LF cost: " + str(sim_avg_lf))
    print("LF cost std dev: " + str(sim_std_lf))
    print("LF cost median: " + str(sim_med_lf))
    print()
    print('Average total: ' + str(numpy.average(totals)))
    print('Total std dev: ' + str(numpy.std(totals)))
    print('Total Median: ' + str(numpy.median(totals)))
    print()
    print('')
    #with file:
        #file.write("LF ," + str(lfs) + "\n ")
        #file.write("RATES ," + str(install_rates) + "\n")
        #file.write("CORNERS ," + str(corners) + "\n")
        #file.write("TOTAL ," + str(totals) + "\n")
        #file.write("$/LF ," + str(per_lfs) + "\n")
        #file.close()
        
    print()
    print()
    return round(sim_avg_lf)
    #start()

#run = start()


