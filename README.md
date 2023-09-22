# Markov Generator
**Description:** This is a Generator program that generates text using a Markov-based algorithm, which predicts the next word based on the probability of occurrence in a given sequence of words

**1. Overview:**

This program will consist: 
- A `Parameter` section that includes functions to modify words 
- The `TextModel` class blueprint for objects that model a body of text
- A `Testing` sections that serves to test the program
--- 

**2. Program Specifications:**

- **Input Format:** A sample TXT file with paragraphs or words of any amount 

- **Output Format:** The program will print out a paragraph of _n_ words (specified by user) of complete sentences generated through referenceing the TXT file
---

#### **Code Specifications:**
- **create_dictionary(filename):** This method takes a string representing the name of a text file, 
    and that returns a dictionary of key-value pairs in which:
  
- **generate_text(word_dict, num_words):** This method use word_dict to generate and 
    print num_words words, with a space after each word.
  
---

**4. Example:**

Below is an example testing the program: 
Function name: `generate_text(word_dict, num_words):`
```
# Create random text from lyrics from the song Brave by Sara Bareilles

word_dict = create_dictionary('sample_text.txt')

generate_text(word_dict, 20)

```

**5. Usage/Installation:**

- **1: Clone Repository:** 
  ```
  git clone https://github.com/jasonjiang9142/MarkovGenerator.git
  ```

- **2: Just run the program in any Virtual Environment** 


