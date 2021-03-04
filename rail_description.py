

rail_height = ['36"','42"']
post_type = ['2-1/2 x 4" Base shoe','2-3/8" x 2-3/8" square aluminum posts',]
mounting_detail = ["fascia mounted to front of deck framing using PRO's Fascia brackets", 'fascia mounted to front of deck framing using steel angle iron (angle iron installed by others)',
                    'mounted directly to deck framing using engineered lags',' mounted to top of deck surface using rubber gasket and 5x5 baseplate','fascia mounted to welded knife plates (knife plates by others)',
                   'fascia mounted to angle aluminum brakets attached to halfens']
top_rail = ['Top rail profile 200', 'Top rail profile 375','Top rail profile 400','CL Laurence 1" x 1-5/16" SS  Top rail Profile']
bottom_rail = ['with glass clips and bottom rail profile 200',' bottom rail profile 200',' with CR Laurence SS cladding','bottom rail profile 100','bottom rail profile 200 wide']
infill = ['5/8" x 5/8" picket infill','1/4 laminated Tempered glass infill','3/8 laminated Tempered glass infill','1/2 laminated Tempered glass infill','9/16 laminated Tempered glass infill']
spacing = ['',"2'","3'","4'","5'","6'"]
rail_type = ['Grab rail','Hand rail','Picket rail','Glass rail','Cable rail']

def get_description():
    set_height = int(input('0. for 36" \n1. for 42"\n :'))
    set_post = int(input('0. for base shoe\n1. for standard aluminum post\n :'))
    set_mount = int(input('0. for fascia bracket\n1. for fascia steel angle iron\n2. for direct bolt to fascia\n3. for surface mount 5x5\n4. for knife plates\n5. for fascia with halfens and angle brackets\n :'))
    set_top = int(input('0. for TR200\n1. for TR375\n2. for TR400\n3. for CRL SS Glass cap\n :'))
    set_bottom = int(input('0. for glass clip + BR200\n1. for BR200\n2. for SS cladding\n3. for BR100\n4. for BR200 wide\n :'))
    set_infill = int(input('0. for picket\n1. for 1/4 glass\n2. for 3/8 glass\n3. for 1/2 glass\n4. for 9/16 glass\n :'))
    set_spacing = int(input('0. for NA\n1. for 2 foot\n2. for 3 foot\n3. for 4 foot\n4. for 5 foot\n5. for 6 foot\n :'))
    set_type = int(input('0. for grabrail\n1. for handrail\n2. for picket rail\n3. for glass rail\n4. for cable rail\n :'))
    return set_height,set_post,set_mount,set_top,set_bottom,set_infill,set_spacing,set_type

def return_description(set_height,set_post,set_mount,set_top,set_bottom,set_infill,set_spacing,set_type):
    rail_description = []
    rail_description.append(rail_height[set_height])
    rail_description.append(post_type[set_post])
    rail_description.append(mounting_detail[set_mount])
    rail_description.append(top_rail[set_top])
    rail_description.append(bottom_rail[set_bottom])
    rail_description.append(infill[set_infill])
    rail_description.append(spacing[set_spacing])
    rail_description.append(rail_type[set_type])
    return rail_description


