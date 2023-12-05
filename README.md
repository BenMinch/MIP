# MIP: Meaningful Information from Protein Descriptions
A tool to extract meaningful functional information from confusing protein descriptions gathered from PFAM or other databases. This tool has two parts to it: 1) A PFAM scaper to get protein descriptions from PFAM accession numbers. 2) An AI-based classification tool to read those descriptions at scale and summarize the function of the protein in 4 words or less. 

# The PFAM Scraper
A web-scraper for the PFAM database to quickly get protein descriptions from accession numbers
### Dependencies

1. Python packages: Selenium, Pandas
2. Chromedriver: You must have google chrome on your computer and download the corresponding chromedriver for your version. If you don't know which one to get, just get the latest stable download from this [website](https://googlechromelabs.github.io/chrome-for-testing/)

### Inputs

1. A csv file with a column called "AC" with PFAM accession numbers. PFAM accession numbers usually look like PF followed by 5 numbers (i.e. PF05282).
2. The path to your chromedriver executable file (should be a .sh file)

`python PFAM_scraper.py -i test.csv -o testout.csv -cd path/to/chromedriver`

### Outputs

This program will query the PFAM database and find the paragraph description that accompanies most protein families. It will conviniently place this in a csv file for you to look at later. This does take a while if you have many proteins (about 5 seconds per protein). 

# MIP AI: AI characterization of protein function
The AI portion of MIP is a bit more tricky to setup and does require an OpenAI account with sufficient funds as running GPT models isn't a free service. The cost however is very cheap and shouldn't dissuade you (It is only about 0.024 cents per protein, meaning you can annotate over 4,000 proteins for $1.). This program was built using a custom GPT 3.5 turbo assistant.

### Dependencies
1. Python packages: Pandas, openai
2. An openAI account with a special key

### Instructions for setting up the API key
1. Make sure your openAI account has sufficient funds for your project.
2. Create a new API key by following this [tutorial](https://help.openai.com/en/articles/4936850-where-do-i-find-my-api-key)
3. Add the Key to your bash profile: `nano ~/.bash_profile` and then type this into your bash profile `export OPENAI_API_KEY='your-api-key-here'`
4. Activate your bash profile: `source ~/.bash_profile`
5. Verify your key is active by running: `echo $OPENAI_API_KEY`

### Inputs
1. A csv file with a column called Description. This can be the output of the first protein description scraper tool. This Description can also just be a paragraph or sentence description of a protein you get from any database.

`python MIP_AI.py -i testout.csv -o AI_out.csv`

### Outputs
1. This AI is trained to give you a description of your protein in 4 words or less. It will store this in a column called function. This program can also take some time (about 5 seconds per protein).

