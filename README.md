# county_in_states
The product of my first data project. I wanted to find what counties appeared in more than one state. 
Unsurprisingly, counties named after the founders, or in a few cases: counties named after English aristocrats, appeared in the most states. 
I wrote two functions to acheive this. 

    print(in_state("Bergen"))
    Bergen is only in ['New Jersey']

    print(in_state("York"))
    ['Maine', 'South Carolina', 'Virginia', 'Nebraska', 'Pennsylvania']

    print(in_state("Washington"))
    ['Kentucky', 'Louisiana', 'Maine', 'Iowa', 'Kansas', 'Mississippi', 'Missouri', 'Maryland', 'Minnesota', 'Florida', 'Colorado', 'Alabama', 'Arkansas', 'Illinois', 'Indiana', 'Idaho', 'Georgia', 'Tennessee', 'Virginia', 'Wisconsin', 'Utah', 'Vermont', 'Texas', 'New York', 'North Carolina', 'Nebraska', 'Pennsylvania', 'Oregon', 'Rhode Island', 'Oklahoma', 'Ohio']

I validated the input against a fixed list of states to avoid errors by using pandas' .unique() method. 
The variable 'states' referenced in the if statement below was df.state.unique().

    def counties_in(state):
        counties = df[df['state'] == state].county.unique()
        if state not in states:
            return "{0} is not a state.".format(state)
        return counties
        
Then I wrote essentially an inverse of the previous function.
I created a dateframe for a given county. 
Then I added the .unique() method to the county_df.state column,
to return a list of states where the counties appeared. 

    def in_state(county):
        county_df = df[df['county'] == county]
        also_in = county_df.state.unique().tolist()
        states = county_df.state.unique()
        if len(also_in) > 1:
            return also_in
        if len(also_in) <= 1:
            return "{0} is only in {1}".format(county, states)
