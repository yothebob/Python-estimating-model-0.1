from docx import Document
from datetime import date
from docx.shared import Pt, Inches,RGBColor
import sys
import rail_description as rd


# Document Variables
customer_name = 'Jane Doe ' #input('customer rep name?\n :')
customer_company = 'INCLINE Construction' #input('customer company name?\n :')
contact_info = ['971-111-1111','Janedoe@incline-cc.com'] #input('customer contact info?\n :')
company_address = '1234 Place, Portland OR' #input('customer Business address?\n :')
job_address = '5678 work st, tigard OR' #input('job site address?\n :')
job_name = 'Big School Elementary Improvements' #input('Job name?\n :')

#file = open('customer_detail.txt','r')

#with file:
#    customer_name = file.readline()
#    customer_company = file.readline()
#    contact_info = file.readline()
#    company_address = file.readline()
#    job_address = file.readline()
#    job_name = file.readline()

#file.close()

today = date.today()
d1 = today.strftime("%m/%d/%Y")

total_info = [d1,customer_name,contact_info,customer_company,company_address,job_name,job_address]


def menu():
    enter = input('make proposal? (y/n): ')
    if enter.lower() == 'y':
        write_proposal(40,400,100,150)
    elif enter.lower() == 'n':
        sys.exit()
    else:
        print('please try again')
        menu()



def write_proposal(b1_lf,b1_cost,b2_lf,b2_cost):
    print('start making proposal...')
    #Document Setup
    document = Document()

    style = document.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)

    paragraph_format = style.paragraph_format
    paragraph_format.space_before = Pt(3.4)
    paragraph_format.space_after = Pt(0)

    sections = document.sections
    for section in sections:
        section.top_margin = Inches(.5)
        section.bottom_margin = Inches(.4)
        section.left_margin = Inches(.8)
        section.right_margin = Inches(.8)


    #header setup
    header = document.sections[0].header
    h1 = header.paragraphs[0].add_run("\tPrecision Rail of Oregon, LLC\n").font.size = Pt(36)#\n10735 SE Foster RD \t\tPortland, Oregon 97266"
    h2 = header.paragraphs[0].add_run("10735 SE Foster RD").font.size = Pt(14)
    header.paragraphs[0].add_run('\t').add_picture('Alumarail_logo.png', width = Inches(1.8))
    h3 = header.paragraphs[0].add_run("\tPortland, Oregon 97266").font.size = Pt(14)
    h1.italic = True
    h2.italic = True
    h3.italic = True
    h1.bold = True
    h2.bold = True
    h3.bold = True
    header.paragraphs[0].style.font.color.rgb = RGBColor(0, 96, 43)

    #footer setup
    footer = document.sections[0].footer
    footer.paragraphs[0].add_run('Phone: 503-512-5353\tFax: 503-668-8968\twww.Precisionrail.com').font.size = Pt(14)
    footer.paragraphs[0].style.font.color.rgb = RGBColor(0, 96, 43)

    # start Document
    document.add_paragraph('\n')
    for item in total_info:
        document.add_paragraph(str(item))

    document.add_paragraph('')
    document.add_paragraph('Dear ' + customer_name + ',\n')

    p1 = document.add_paragraph()
    p1.style = document.styles['Normal']
    
    
    p1.add_run('Precision Rail of Oregon is pleased to provide the following proposal for: ')
    p1.add_run(job_name + ', BUDGET Rev-0 \n\n').bold = True
    p1.add_run('Items furished by Precision Rail of Oregon: Submittal drawings, engineering, materials, and installation.\n\n').bold = True
    p1.add_run('Submittals:').bold = True
    p1.add_run(' Pricing includes 1 submittal based off plans and 1 revision once corrections are recieved from GC. Any Additional revisions to be billed at 145.00 per hour plus materials and handling. \n\n')

    b1_height,b1_post,b1_mount,b1_top,b1_bottom,b1_infill,b1_space,b1_type = rd.get_description()
    b1 = rd.return_description(b1_height,b1_post,b1_mount,b1_top,b1_bottom,b1_infill,b1_space,b1_type)
    
    p1.add_run('Bid Item - {}, {} \n'.format(b1[0],b1[7])).bold = True
    p1.add_run("{} Tall {} {}. {}, {}, {}. Posts spacing to be spaced evenly and not exceed {} per engineering and customer request. Support blocking by others. Standard color(Black, Bronze, White).".format(b1[0],b1[1],b1[2],b1[3],b1[4],b1[5],b1[6])) 
        
    p1.add_run('\n\n')
    p1.add_run('\t\t\t\t\t\tTotal {} LF @ $ {} per LF = $ {} *\n\n\n'.format(str(b1_lf),str(b1_cost),str(b1_lf*b1_cost))).bold = True

    b2_height,b2_post,b2_mount,b2_top,b2_bottom,b2_infill,b2_space,b2_type = rd.get_description()
    b2 = rd.return_description(b2_height,b2_post,b2_mount,b2_top,b2_bottom,b2_infill,b2_space,b2_type)    
    
    p1.add_run('Bid Item - {}, {} \n'.format(b2[0],b2[7])).bold = True
    p1.add_run("{} Tall {} {}. {}, {}, {}. Posts spacing to be spaced evenly and not exceed {} Per engineering and customer request. Support blocking by others. Standard color(Black, Bronze, White).".format(b2[0],b2[1],b2[2],b2[3],b2[4],b2[5],b2[6]))
    p1.add_run('\n\n')
    p1.add_run('\t\t\t\t\t\tTotal {} LF @ $ {} per LF = $ {}*\n\n\n'.format(str(b2_lf),str(b2_cost),str(b2_cost * b2_lf))).bold = True

    p1.add_run('\n\n\n')
    p1.add_run('\t\t\t\t\t\t\t\t\tSub Total = {}*\n\n\n'.format(str((b1_cost * b1_lf) + (b2_cost * b2_lf)))).bold = True
    
    
    p1.add_run('*This price quote is valid for 3 months from the date of this document*\n\n').italic = True

    p1.add_run('Assumptions\n').bold = True
    p1.add_run('The following assumptions were made in support of this estimate:')


    p1.add_run(
                """
        1.	Electrical utilities available on site.
        2.	Sanitation facilities will be provided and available on site.
        3.	Core holes, provided by others, will be cleaned out and ready for post installation.
        4.	Fall restraint anchor points will be available and cleaned out ready for use.
        5.	Paint / PPG Duracron with a 5 year warranty.
                """)
    p1.add_run('\n')
    p1.add_run('Items EXCLUDED by precision rail of oregon unless noted above:')

    p1.add_run(
        """
        1.	Deferred permits or any items not specifically included is considered furnished by others.
        2.	Taxes such as sales, local municipality, gross receipts tax and/or local business licenses.
        3.	Union, prevailing wage and/or workforce training installation
        4.	Insurance requirements above and beyond: $1M/$2M (occurrence/aggregate); and $3M
            umbrella.
        5.	Performance & payment bonds.
        6.	Pollution insurance requirements.
        7.	Deviations from project plans that impede the installation of our rail as planned.
        8.	Marking / locating rebar tensions wires
        9.	Coverage / Protection of any Glazing, Brick, Building materials
        10. Inspection for testing (example UT, NDT & others)
        11. Flaggers, and / or any personnel for traffic control
        12. Lifts, swing stages, cranes, or other equipment required to install are not included in this bid
                and are to be provided by the GC.

        """)
    p1.add_run('\n\n')

    p1.add_run("Submittal drawings with approval by the representative of buyer (customer) or owner shall be considered the correct measurement and method for fabrication. Delivery schedule will be based on receipt of final approved submittal drawings.\n\nThank you for the opportunity to submit a proposal.\n\nSincerely,")
    document.add_picture('JAG_signature.png', width=Inches(2))

    sign = document.add_paragraph()
    sign.style = document.styles['Normal']
    sign.add_run('Jeff Garlitz\n')
    sign.add_run('jgarlitz@precisionrail.com\n')
    sign.add_run('541-279-8182\n')
    sign.add_run('This estimate was computer generated by Brandon Brodrick').italic = True
    sign.add_run('\n\n\n')
    sign.add_run('Acceptance of Proposal Signature _______________________              Date_______________   ')

    document.save('testing.docx')
    print('proposal finished!')
        
        
#menu()
    
