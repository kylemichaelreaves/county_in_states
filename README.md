# county_in_states
A reverse engineered python dictionary where the key is the county and the values are the states where the county appears. 
I was interested in seeing what counties appeared in other states and at what frequency. 

For example:
    
    print(in_state("Bergen"))
    Bergen is only in ['New Jersey']

    print(in_state("York"))
    ['Maine', 'South Carolina', 'Virginia', 'Nebraska', 'Pennsylvania']


    print(in_state("Washington"))
    ['Kentucky', 'Louisiana', 'Maine', 'Iowa', 'Kansas', 'Mississippi', 'Missouri', 'Maryland', 'Minnesota', 'Florida', 'Colorado', 'Alabama', 'Arkansas', 'Illinois', 'Indiana', 'Idaho', 'Georgia', 'Tennessee', 'Virginia', 'Wisconsin', 'Utah', 'Vermont', 'Texas', 'New York', 'North Carolina', 'Nebraska', 'Pennsylvania', 'Oregon', 'Rhode Island', 'Oklahoma', 'Ohio']



The original dictionary was built from a covid-19 dataframe, after it had appeared in every county in the US. 
I wrote a function to return the counties in an inputted state. I validated the input against a fixed list of states to avoid errors. 

    def counties_in(state):
        counties = df[df['state'] == state].county.unique()
        if state not in states:
            return "{0} is not a state.".format(state)
        return counties
        
Then I wrote essentially an inverse of the previous function, and finally looped through a list of all the counties in the covid-19 dataframe,
from which I built the counties_in_states.py dict. 

    def in_state(county):
        county_df = df[df['county'] == county]
        also_in = county_df.state.unique().tolist()
        states = county_df.state.unique()
        if len(also_in) > 1:
            return also_in
        if len(also_in) <= 1:
            return "{0} is only in {1}".format(county, states)
