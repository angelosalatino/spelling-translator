import json
import re


class Spelling_Translator:
    """ Spelling translator class from British to American and viceversa."""
    
    def __init__(self):
        self.uk2us_spelling = None
        self.us2uk_spelling = None
        
        self.regex = r"[a-zA-Z]*"
        
        self._load_uk2us()
        
    
    def _load_uk2us(self):
        """
        Load the spelling mapping UK -> US

        Returns
        -------
        None.

        """
        with open('uk2us.json','r') as f_r:
            self.uk2us_spelling = json.load(f_r)
    
        
    def _create_us2uk(self):
        """
        Create the opposite spelling mapping US -> UK
    
        Returns
        -------
        None.

        """
        self.us2uk_spelling = dict()
        for k,v in self.uk2us_spelling.items():
            self.us2uk_spelling[v] = k
    
    def translate_to_american(self, text_to_process:str) -> str:
        """
        

        Parameters
        ----------
        text_to_process : str
            input text in British spelling to convert to American Spelling.

        Returns
        -------
        str
            The processed text.

        """
        text_to_process = text_to_process.lower()
        matches = re.findall(self.regex, text_to_process, re.MULTILINE)
        matches = list(filter(None, matches))
        
        for match in matches:
            if match in self.uk2us_spelling:
                text_to_process = text_to_process.replace(match,self.uk2us_spelling[match],1)

        return text_to_process     
    
    def translate_to_british(self, text_to_process:str) -> str:
        """
        

        Parameters
        ----------
        text_to_process : str
            input text in American spelling to convert to British Spelling.

        Returns
        -------
        str
            The processed text.

        """
        if self.us2uk_spelling is None:
            self._create_us2uk()
            
        text_to_process = text_to_process.lower()
        matches = re.findall(self.regex, text_to_process, re.MULTILINE)
        matches = list(filter(None, matches))
        
        for match in matches:
            if match in self.us2uk_spelling:
                text_to_process = text_to_process.replace(match,self.us2uk_spelling[match],1)

        return text_to_process    
    
    def test(self):
        """
        Testing class

        Returns
        -------
        None.

        """
        test = "I realise I can see the world in colour but I can't vocalise its splendour"
        print(f"Intial Sentence: {test}")
        test_american = self.translate_to_american(test)
        print(f"Sentence converted in America Spelling: {test_american}")
        test_british = self.translate_to_british(test_american)
        print(f"Sentence re-converted in British Spelling: {test_british}")
        
        
def main():
    """
    Main function
    """
    st = Spelling_Translator()
    st.test()
    

if __name__ == '__main__':
    main()