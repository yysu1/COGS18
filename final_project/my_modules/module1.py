import string


proteins= ['beef','chicken','pork','tofu','tempeh']
dietary_restrictions= ['vegan','gluten-free','both']
carbs= ['pasta/noodles','couscous','rice','potatoes','sweet potatoes','gluten-free pasta/noodles']
cuisines= ['thai','chinese','mediterranean','italian','indian','mexican']
veggies= ['green beans','cauliflower','tomato','bell peppers', 'snow peas','corn']
neg_responses= ['no','nope','not','none'] 


def remove_punctuation(input_string):
    out_string=''
    for characters in input_string:
        if characters =='-':
            out_string=out_string+characters
        elif characters not in string.punctuation:
            out_string=out_string+characters
    return out_string


def check_if_in_list(input_string, check_list):
    '''evaluate if any word in input_string match item in check_list.
    
    Parameters
    ----------
    input_string: str
         function will take every word from this string to match with every item in check_list
    check_list: list
         list consists of items that serve as the reference for matching
                      
    Returns
    ----------
    output: dict
        contains two keys: 'in_list' and 'item'
        'in_list' stores True if there is a successful match
        'in_list' stores False if none of the words in input_string match any item in check_list
        'item' store the item that input_string and check_list have in common
    '''
    output=dict()
    temp_string=input_string.lower()
    output['in_list'] =False
    input_to_list=temp_string.split()
    for item in input_to_list:
        if item in check_list:
            output['in_list']=True
            output['item']=item
    return output


def show_options(option_list):
    for option in option_list:
        print("-"+option)
        

        
 #I use the website below as reference
 #https://www.digitalocean.com/community/tutorials/how-to-scrape-web-pages-with-beautiful-soup-and-python-3
def find_spice(cuisine):
    '''print a list of spices relevant to the input cuisine 
        depending on the cuisine, this function will return different part of the content from a cooking website
    
    Parameters
    ----------
    cuisine: str
        the cuisine will determine which spices will be included in the list returned
    
    Returns
    ----------
    list_of_spices: list
        this list contains spices specific to the cuisine sourced from the website
        
    Warning
    ----------
    this function uses bs4 to pull data from https://www.spicesinc.com/p-3746-most-popular-spices-by-cuisine.aspx
    index to specify which section of the website will be printed
    changes to the website can cause index to be inaccurate
   
    '''
    import requests
    from bs4 import BeautifulSoup
    page = requests.get('https://www.spicesinc.com/p-3746-most-popular-spices-by-cuisine.aspx')
    soup = BeautifulSoup(page.text, 'html.parser')
    spice_list = soup.find(class_='tabs')
    spice_item_list=spice_list.find_all('a')
    list_of_spices=[]

    if cuisine=='chinese':
        for spice in spice_item_list[58:70]:
            spice_name = spice.contents[0]
            list_of_spices.append(spice_name)
    
    if cuisine=='indian':
        for spice in spice_item_list[76:113]:
            spice_name = spice.contents[0]
            list_of_spices.append(spice_name)
            
    if cuisine=='italian':
        for spice in spice_item_list[117:123]:
            spice_name = spice.contents[0]
            list_of_spices.append(spice_name)
            
    if cuisine=='mediterranean':
        for spice in spice_item_list[128:162]:
            spice_name = spice.contents[0]
            list_of_spices.append(spice_name)
            
    if cuisine=='mexican':
        for spice in spice_item_list[168:183]:
            spice_name = spice.contents[0]
            list_of_spices.append(spice_name)
    
    if cuisine=='thai':
        for spice in spice_item_list[237:256]:
            spice_name = spice.contents[0]
            list_of_spices.append(spice_name)
    return list_of_spices
    
  
        