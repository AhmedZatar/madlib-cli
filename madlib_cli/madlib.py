
import re
def read_template(path):
    """
    Recursive function take path and read the file
    Arguments:
        path:string -- path of the used file
    Returns:
        text inside the file 
    """
    try:
        with open(path) as file:
            return  file.read()
    except FileNotFoundError:
        raise FileNotFoundError('The file not found')
    except Exception as e:
        return "Something's Going Wrong : "+ e

def parse_template(text):
    """
    Recursive function take text and put anything inside {} in tuple and remove it frome text
    Arguments:
        text:string -- text file or a text
    Returns:
        1-text with removing anythings inside {}
        2- anythings inside {} in tuple
    """
    parse= re.findall(r'\{(.*?)\}', text)
    for item in parse:    
        text=text.replace((item),'',1)
    return text, tuple(parse)


def merge(text,parse):
    """
    Recursive function format a tuple inside text
    Arguments:
        text:string -- text with empty {}
        parse:tuple -- tuple of strings or numbers
    Returns:
        text with formated tuple inside it
    """
    updatedText=text.format(*parse)

    with open('assets/make_me_a_video_game_output.txt','w') as output:
        output.write(updatedText)
    return updatedText

def the_game():

    """
    Recursive function for run the game       
    Returns:
        text with formated tuple inside it
    """

    print('Hello And Welcome to Madlib Game, Input requirements')
    print('I hope you enjoy it :)\n')

    text_As_String=read_template('assets/make_me_a_video_game_template.txt')

    text,parse= parse_template(text_As_String)
    input_list=[]
    for i in parse:
        user_input=input(f'Enter a {i} ')
        input_list.append(user_input)
    
    text_output=merge(text,input_list)
    
    return text_output

if __name__=='__main__':
  print (the_game())


