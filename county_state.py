duplicates_dict = {
    'Adair': 'Kentucky, Iowa, Missouri, Oklahoma',
    'Adams': 'Iowa, Mississippi, Colorado, Illinois, Indiana, Idaho, Washington, Wisconsin, Nebraska, Pennsylvania, Ohio',
    'Albany': 'Wyoming, New York',
    'Alexander': 'Illinois, North Carolina',
    'Allegany': 'Maryland, New York',
    'Alleghany': 'Virginia, North Carolina',
    'Allen': 'Kentucky, Louisiana, Kansas, Indiana, Ohio',
    'Anderson': 'Kentucky, Kansas, Tennessee, Texas, South Carolina',
    'Armstrong': 'Texas, Pennsylvania',
    'Ashland': 'Wisconsin, Ohio',
    'Atchison': 'Kansas, Missouri',
    'Baker': 'Florida, Georgia, Oregon',
    'Baldwin': 'Alabama, Georgia',
    'Barbour': 'Alabama, West Virginia',
    'Barry': 'Missouri, Michigan',
    'Barton': 'Kansas, Missouri',
    'Bay': 'Michigan, Florida',
    'Beaufort': 'North Carolina, South Carolina',
    'Beaver': 'Utah, Pennsylvania, Oklahoma',
    'Bedford': 'Tennessee, Virginia, Pennsylvania',
    'Bell': 'Kentucky, Texas',
    'Benton': 'Iowa, Mississippi, Missouri, Minnesota, Arkansas, Indiana, Tennessee, Washington, Oregon',
    'Berkeley': 'West Virginia, South Carolina',
    'Berrien': 'Michigan, Georgia',
    'Bibb': 'Alabama, Georgia',
    'Big Horn': 'Wyoming, Montana',
    'Blaine': 'Idaho, Oklahoma',
    'Blount': 'Alabama, Tennessee',
    'Boone': 'Kentucky, Iowa, Missouri, Arkansas, Illinois, Indiana, West Virginia, Nebraska',
    'Bourbon': 'Kentucky, Kansas',
    'Boyd': 'Kentucky, Nebraska',
    'Bradford': 'Florida, Pennsylvania',
    'Bradley': 'Arkansas, Tennessee',
    'Bristol': 'Massachusetts, Rhode Island',
    'Brooks': 'Georgia, Texas',
    'Brown': 'Kansas, Minnesota, Illinois, Indiana, South Dakota, Texas, Wisconsin, Ohio',
    'Brunswick': 'Virginia, North Carolina',
    'Bryan': 'Georgia, Oklahoma',
    'Buchanan': 'Iowa, Missouri, Virginia',
    'Buffalo': 'South Dakota, Wisconsin, Nebraska',
    'Burke': 'Georgia, North Carolina, North Dakota',
    'Butler': 'Kentucky, Iowa, Kansas, Missouri, Alabama, Nebraska, Pennsylvania, Ohio',
    'Caddo': 'Louisiana, Oklahoma',
    'Caldwell': 'Kentucky, Louisiana, Missouri, Texas, North Carolina',
    'Calhoun': 'Iowa, Mississippi, Michigan, Florida, Alabama, Arkansas, Illinois, Georgia, Texas, West Virginia, South Carolina',
    'Camden': 'Missouri, Georgia, New Jersey, North Carolina',
    'Cameron': 'Louisiana, Texas, Pennsylvania',
    'Campbell': 'Kentucky, Tennessee, Wyoming, Virginia',
    'Carbon': 'Wyoming, Utah, Montana, Pennsylvania',
    'Caroline': 'Maryland, Virginia',
    'Carroll': 'Kentucky, Iowa, Mississippi, Missouri, Maryland, Arkansas, Illinois, Indiana, Georgia, Tennessee, Virginia, New Hampshire, Ohio',
    'Carter': 'Kentucky, Missouri, Tennessee, Oklahoma',
    'Cass': 'Iowa, Missouri, Michigan, Minnesota, Illinois, Indiana, Texas, Nebraska, North Dakota',
    'Cedar': 'Iowa, Missouri, Nebraska',
    'Chambers': 'Alabama, Texas',
    'Champaign': 'Illinois, Ohio',
    'Charlotte': 'Florida, Virginia',
    'Chase': 'Kansas, Nebraska',
    'Chatham': 'Georgia, North Carolina',
    'Chautauqua': 'Kansas, New York',
    'Cherokee': 'Iowa, Kansas, Alabama, Georgia, Texas, North Carolina, South Carolina, Oklahoma',
    'Chester': 'Tennessee, Pennsylvania, South Carolina',
    'Chesterfield': 'Virginia, South Carolina',
    'Cheyenne': 'Kansas, Colorado, Nebraska',
    'Chickasaw': 'Iowa, Mississippi',
    'Chippewa': 'Michigan, Minnesota, Wisconsin',
    'Choctaw': 'Mississippi, Alabama, Oklahoma',
    'Christian': 'Kentucky, Missouri, Illinois',
    'Claiborne': 'Louisiana, Mississippi, Tennessee',
    'Clark': 'Kentucky, Kansas, Missouri, Arkansas, Illinois, Indiana, South Dakota, Washington, Wisconsin, Nevada, Ohio',
    'Clarke': 'Iowa, Mississippi, Alabama, Georgia, Virginia',
    'Clay': 'Kentucky, Iowa, Kansas, Mississippi, Missouri, Minnesota, Florida, Alabama, Arkansas, Illinois, Indiana, Georgia, Texas, Tennessee, South Dakota, West Virginia, North Carolina, Nebraska',
    'Clayton': 'Iowa, Georgia',
    'Clearwater': 'Minnesota, Idaho',
    'Cleburne': 'Alabama, Arkansas',
    'Cleveland': 'Arkansas, North Carolina, Oklahoma',
    'Clinton': 'Kentucky, Iowa, Missouri, Michigan, Illinois, Indiana, New York, Pennsylvania, Ohio',
    'Coffee': 'Alabama, Georgia, Tennessee',
    'Colfax': 'New Mexico, Nebraska',
    'Columbia': 'Florida, Arkansas, Georgia, Washington, Wisconsin, New York, Oregon, Pennsylvania',
    'Comanche': 'Kansas, Texas, Oklahoma',
    'Cook': 'Minnesota, Illinois, Georgia',
    'Coos': 'New Hampshire, Oregon',
    'Covington': 'Mississippi, Alabama',
    'Craig': 'Virginia, Oklahoma',
    'Crawford': 'Iowa, Kansas, Missouri, Michigan, Arkansas, Illinois, Indiana, Georgia, Wisconsin, Pennsylvania, Ohio',
    'Crittenden': 'Kentucky, Arkansas',
    'Crockett': 'Texas, Tennessee',
    'Crook': 'Wyoming, Oregon',
    'Cumberland': 'Kentucky, Maine, Illinois, Tennessee, Virginia, New Jersey, North Carolina, Pennsylvania',
    'Curry': 'New Mexico, Oregon',
    'Custer': 'Colorado, Idaho, South Dakota, Montana, Nebraska, Oklahoma',
    'Dade': 'Missouri, Georgia',
    'Dakota': 'Minnesota, Nebraska',
    'Dallas': 'Iowa, Missouri, Alabama, Arkansas, Texas',
    'Davidson': 'Tennessee, North Carolina',
    'Daviess': 'Kentucky, Missouri, Indiana',
    'Davis': 'Iowa, Utah',
    'Dawson': 'Georgia, Texas, Montana, Nebraska',
    'DeKalb': 'Missouri, Alabama, Illinois, Indiana, Georgia, Tennessee',
    'DeSoto': 'Mississippi, Florida',
    'Decatur': 'Iowa, Indiana, Georgia, Tennessee',
    'Delaware': 'Iowa, Indiana, New York, Pennsylvania, Ohio, Oklahoma',
    'Delta': 'Michigan, Colorado, Texas',
    'Dewey': 'South Dakota, Oklahoma',
    'Dickinson': 'Iowa, Kansas, Michigan',
    'Dodge': 'Minnesota, Georgia, Wisconsin, Nebraska',
    'Dorchester': 'Maryland, South Carolina',
    'Douglas': 'Kansas, Missouri, Minnesota, Colorado, Illinois, Georgia, South Dakota, Washington, Wisconsin, Nevada, Nebraska, Oregon',
    'Dunn': 'Wisconsin, North Dakota',
    'Duval': 'Florida, Texas',
    'Eddy': 'New Mexico, North Dakota',
    'Edwards': 'Kansas, Illinois, Texas',
    'Effingham': 'Illinois, Georgia',
    'El Paso': 'Colorado, Texas',
    'Elbert': 'Colorado, Georgia',
    'Elk': 'Kansas, Pennsylvania',
    'Ellis': 'Kansas, Texas, Oklahoma',
    'Elmore': 'Alabama, Idaho',
    'Emmet': 'Iowa, Michigan',
    'Erie': 'New York, Pennsylvania, Ohio',
    'Escambia': 'Florida, Alabama',
    'Essex': 'Massachusetts, Vermont, Virginia, New York, New Jersey',
    'Fairfield': 'Connecticut, South Carolina, Ohio',
    'Fannin': 'Georgia, Texas',
    'Fayette': 'Kentucky, Iowa, Alabama, Illinois, Indiana, Georgia, Texas, Tennessee, West Virginia, Pennsylvania, Ohio',
    'Fillmore': 'Minnesota, Nebraska',
    'Florence': 'Wisconsin, South Carolina',
    'Floyd': 'Kentucky, Iowa, Indiana, Georgia, Texas, Virginia',
    'Ford': 'Kansas, Illinois',
    'Forest': 'Wisconsin, Pennsylvania',
    'Forsyth': 'Georgia, North Carolina',
    'Franklin': 'Kentucky, Louisiana, Iowa, Kansas, Mississippi, Missouri, Massachusetts, Maine, Florida, Alabama, Arkansas, Illinois, Indiana, Georgia, Idaho, Texas, Tennessee, Washington, Vermont, Virginia, New York, North Carolina, Nebraska, Pennsylvania, Ohio',
    'Frederick': 'Maryland, Virginia',
    'Fremont': 'Iowa, Colorado, Idaho, Wyoming',
    'Fulton': 'Kentucky, Arkansas, Illinois, Indiana, Georgia, New York, Pennsylvania, Ohio',
    'Gallatin': 'Kentucky, Illinois, Montana',
    'Garfield': 'Colorado, Utah, Nebraska, Oklahoma',
    'Genesee': 'Michigan, New York',
    'Gibson': 'Indiana, Tennessee',
    'Giles': 'Tennessee, Virginia',
    'Gilmer': 'Georgia, West Virginia',
    'Gloucester': 'Virginia, New Jersey',
    'Grady': 'Georgia, Oklahoma',
    'Graham': 'Arizona, North Carolina',
    'Grand': 'Colorado, Utah',
    'Grant': 'Kentucky, Louisiana, Kansas, Minnesota, Arkansas, Indiana, South Dakota, West Virginia, Washington, Wisconsin, New Mexico, Oregon, North Dakota, Oklahoma',
    'Gray': 'Kansas, Texas',
    'Grayson': 'Kentucky, Texas, Virginia',
    'Green': 'Kentucky, Wisconsin',
    'Greene': 'Iowa, Mississippi, Missouri, Alabama, Arkansas, Illinois, Indiana, Georgia, Tennessee, Virginia, New York, North Carolina, Pennsylvania, Ohio',
    'Greenwood': 'Kansas, South Carolina',
    'Grundy': 'Iowa, Missouri, Illinois, Tennessee',
    'Guadalupe': 'Texas, New Mexico',
    'Hale': 'Alabama, Texas',
    'Halifax': 'Virginia, North Carolina',
    'Hall': 'Georgia, Texas, Nebraska',
    'Hamilton': 'Iowa, Kansas, Florida, Illinois, Indiana, Texas, Tennessee, New York, Nebraska, Ohio',
    'Hampshire': 'Massachusetts, West Virginia',
    'Hancock': 'Kentucky, Iowa, Mississippi, Maine, Illinois, Indiana, Georgia, Tennessee, West Virginia, Ohio',
    'Hardeman': 'Texas, Tennessee',
    'Hardin': 'Kentucky, Iowa, Illinois, Texas, Tennessee, Ohio',
    'Harlan': 'Kentucky, Nebraska',
    'Harper': 'Kansas, Oklahoma',
    'Harris': 'Georgia, Texas',
    'Harrison': 'Kentucky, Iowa, Mississippi, Missouri, Indiana, Texas, West Virginia, Ohio',
    'Hart': 'Kentucky, Georgia',
    'Haskell': 'Kansas, Texas, Oklahoma',
    'Haywood': 'Tennessee, North Carolina',
    'Henderson': 'Kentucky, Illinois, Texas, Tennessee, North Carolina',
    'Henry': 'Kentucky, Iowa, Missouri, Alabama, Illinois, Indiana, Georgia, Tennessee, Virginia, Ohio',
    'Hickman': 'Kentucky, Tennessee',
    'Hidalgo': 'Texas, New Mexico',
    'Highland': 'Virginia, Ohio',
    'Hill': 'Texas, Montana',
    'Hillsborough': 'Florida, New Hampshire',
    'Holmes': 'Mississippi, Florida, Ohio',
    'Holt': 'Missouri, Nebraska',
    'Hopkins': 'Kentucky, Texas',
    'Houston': 'Minnesota, Alabama, Georgia, Texas, Tennessee',
    'Howard': 'Iowa, Missouri, Maryland, Arkansas, Indiana, Texas, Nebraska',
    'Hughes': 'South Dakota, Oklahoma',
    'Humboldt': 'Iowa, California, Nevada',
    'Humphreys': 'Mississippi, Tennessee',
    'Huron': 'Michigan, Ohio',
    'Hutchinson': 'Texas, South Dakota',
    'Hyde': 'South Dakota, North Carolina',
    'Iowa': 'Iowa, Wisconsin',
    'Iron': 'Missouri, Michigan, Wisconsin, Utah',
    'Jackson': 'Kentucky, Louisiana, Iowa, Kansas, Mississippi, Missouri, Minnesota, Michigan, Colorado, Florida, Alabama, Arkansas, Illinois, Indiana, Georgia, Texas, South Dakota, Tennessee, West Virginia, Wisconsin, North Carolina, Oregon, Oklahoma, Ohio',
    'Jasper': 'Iowa, Mississippi, Missouri, Illinois, Indiana, Georgia, Texas, South Carolina',
    'Jeff Davis': 'Georgia, Texas',
    'Jefferson': 'Kentucky, Louisiana, Iowa, Kansas, Mississippi, Missouri, Colorado, Florida, Alabama, Arkansas, Illinois, Indiana, Georgia, Idaho, Texas, Tennessee, West Virginia, Washington, Wisconsin, New York, Montana, Nebraska, Oregon, Oklahoma, Pennsylvania, Ohio',
    'Jefferson Davis': 'Louisiana, Mississippi',
    'Johnson': 'Kentucky, Iowa, Kansas, Missouri, Arkansas, Illinois, Indiana, Georgia, Texas, Tennessee, Wyoming, Nebraska',
    'Johnston': 'North Carolina, Oklahoma',
    'Jones': 'Iowa, Mississippi, Georgia, Texas, North Carolina',
    'Kane': 'Illinois, Utah',
    'Kendall': 'Illinois, Texas',
    'Kent': 'Maryland, Michigan, Delaware, Rhode Island',
    'Kiowa': 'Kansas, Oklahoma',
    'Knox': 'Kentucky, Missouri, Maine, Illinois, Indiana, Texas, Tennessee, Nebraska, Ohio',
    'LaSalle': 'Louisiana, Illinois',
    'Lafayette': 'Louisiana, Mississippi, Missouri, Florida, Arkansas, Wisconsin',
    'Lake': 'Minnesota, Michigan, Colorado, California, Florida, Illinois, Indiana, South Dakota, Tennessee, Montana, Oregon, Ohio',
    'Lamar': 'Mississippi, Alabama, Georgia, Texas',
    'Lancaster': 'Virginia, Nebraska, South Carolina, Pennsylvania',
    'Lane': 'Kansas, Oregon',
    'Lauderdale': 'Mississippi, Alabama, Tennessee',
    'Laurens': 'Georgia, South Carolina',
    'Lawrence': 'Kentucky, Mississippi, Missouri, Alabama, Arkansas, Illinois, Indiana, South Dakota, Tennessee, Pennsylvania, Ohio',
    'Lee': 'Kentucky, Iowa, Mississippi, Florida, Alabama, Arkansas, Illinois, Georgia, Texas, Virginia, North Carolina, South Carolina',
    'Leon': 'Florida, Texas',
    'Lewis': 'Kentucky, Missouri, Tennessee, West Virginia, Washington, New York',
    'Liberty': 'Florida, Georgia, Texas, Montana',
    'Limestone': 'Alabama, Texas',
    'Lincoln': 'Kentucky, Louisiana, Mississippi, Missouri, Maine, Minnesota, Colorado, Arkansas, Idaho, Georgia, South Dakota, Tennessee, West Virginia, Washington, Wyoming, Wisconsin, New Mexico, North Carolina, Montana, Nevada, Nebraska, Oregon, Oklahoma, Kansas',
    'Linn': 'Iowa, Kansas, Missouri, Oregon',
    'Livingston': 'Kentucky, Louisiana, Missouri, Michigan, Illinois, New York',
    'Logan': 'Kentucky, Kansas, Colorado, Arkansas, Illinois, West Virginia, Oklahoma, Ohio',
    'Louisa': 'Iowa, Virginia',
    'Lowndes': 'Mississippi, Alabama, Georgia',
    'Lucas': 'Iowa, Ohio',
    'Lyon': 'Kentucky, Iowa, Kansas, Minnesota, Nevada',
    'Macon': 'Missouri, Alabama, Illinois, Georgia, Tennessee, North Carolina',
    'Madison': 'Kentucky, Louisiana, Iowa, Mississippi, Missouri, Florida, Alabama, Arkansas, Illinois, Idaho, Indiana, Georgia, Texas, Tennessee, Virginia, New York, North Carolina, Montana, Nebraska, Ohio',
    'Marion': 'Kentucky, Iowa, Kansas, Mississippi, Florida, Alabama, Arkansas, Illinois, Indiana, Georgia, Missouri, Texas, Tennessee, West Virginia, Oregon, South Carolina, Ohio',
    'Marquette': 'Michigan, Wisconsin',
    'Marshall': 'Kentucky, Iowa, Kansas, Mississippi, Minnesota, Alabama, Illinois, Indiana, South Dakota, Tennessee, West Virginia, Oklahoma',
    'Martin': 'Kentucky, Minnesota, Florida, Indiana, Texas, North Carolina',
    'Mason': 'Kentucky, Michigan, Illinois, Texas, West Virginia, Washington',
    'McDowell': 'West Virginia, North Carolina',
    'McHenry': 'Illinois, North Dakota',
    'McIntosh': 'Georgia, Oklahoma, North Dakota',
    'McLean': 'Kentucky, Illinois, North Dakota',
    'McPherson': 'Kansas, South Dakota',
    'Meade': 'Kentucky, Kansas, South Dakota',
    'Mecklenburg': 'Virginia, North Carolina',
    'Medina': 'Texas, Ohio',
    'Meigs': 'Tennessee, Ohio',
    'Menard': 'Illinois, Texas',
    'Menominee': 'Michigan, Wisconsin',
    'Mercer': 'Kentucky, Illinois, Missouri, West Virginia, New Jersey, Pennsylvania, North Dakota, Ohio',
    'Miami': 'Kansas, Indiana, Ohio',
    'Middlesex': 'Massachusetts, Connecticut, Virginia, New Jersey',
    'Midland': 'Michigan, Texas',
    'Miller': 'Arkansas, Georgia, Missouri',
    'Mills': 'Iowa, Texas',
    'Mineral': 'Colorado, West Virginia, Nevada',
    'Mississippi': 'Arkansas, Missouri',
    'Mitchell': 'Iowa, Kansas, Georgia, Texas, North Carolina',
    'Monroe': 'Kentucky, Iowa, Mississippi, Michigan, Florida, Alabama, Arkansas, Illinois, Indiana, Georgia, Tennessee, West Virginia, Wisconsin, New York, Missouri, Pennsylvania, Ohio',
    'Montgomery': 'Kentucky, Iowa, Kansas, Mississippi, Maryland, Alabama, Arkansas, Illinois, Indiana, Georgia, Texas, Tennessee, Virginia, New York, North Carolina, Missouri, Pennsylvania, Ohio',
    'Moore': 'Texas, Tennessee, North Carolina',
    'Morgan': 'Kentucky, Colorado, Alabama, Illinois, Indiana, Georgia, Tennessee, West Virginia, Utah, Missouri, Ohio',
    'Morris': 'Kansas, Texas, New Jersey',
    'Morrow': 'Oregon, Ohio',
    'Morton': 'Kansas, North Dakota',
    'Murray': 'Minnesota, Georgia, Oklahoma',
    'Nassau': 'Florida, New York',
    'Nelson': 'Kentucky, Virginia, North Dakota',
    'Nemaha': 'Kansas, Nebraska',
    'Nevada': 'California, Arkansas',
    'Newton': 'Mississippi, Arkansas, Indiana, Georgia, Texas, Missouri',
    'Nicholas': 'Kentucky, West Virginia',
    'Noble': 'Indiana, Oklahoma, Ohio',
    'Northampton': 'Virginia, North Carolina, Pennsylvania',
    'Northumberland': 'Virginia, Pennsylvania',
    'Oconee': 'Georgia, South Carolina',
    'Ohio': 'Kentucky, Indiana, West Virginia',
    'Oldham': 'Kentucky, Texas',
    'Oneida': 'Idaho, Wisconsin, New York',
    'Orange': 'California, Florida, Indiana, Texas, Vermont, Virginia, New York, North Carolina',
    'Orleans': 'Louisiana, Vermont, New York',
    'Osage': 'Kansas, Missouri, Oklahoma',
    'Osceola': 'Iowa, Michigan, Florida',
    'Otero': 'Colorado, New Mexico',
    'Otsego': 'Michigan, New York',
    'Ottawa': 'Kansas, Michigan, Oklahoma, Ohio',
    'Ouachita': 'Louisiana, Arkansas',
    'Owen': 'Kentucky, Indiana',
    'Page': 'Iowa, Virginia',
    'Panola': 'Mississippi, Texas',
    'Park': 'Colorado, Wyoming, Montana',
    'Paulding': 'Georgia, Ohio',
    'Pawnee': 'Kansas, Oklahoma',
    'Pendleton': 'Kentucky, West Virginia',
    'Pennington': 'Minnesota, South Dakota',
    'Perry': 'Kentucky, Mississippi, Alabama, Arkansas, Illinois, Indiana, Tennessee, Missouri, Pennsylvania, Ohio',
    'Phelps': 'Missouri, Nebraska',
    'Phillips': 'Kansas, Colorado, Arkansas',
    'Pickens': 'Alabama, Georgia, South Carolina',
    'Pierce': 'Georgia, Washington, Wisconsin, Nebraska, North Dakota',
    'Pike': 'Kentucky, Mississippi, Alabama, Arkansas, Illinois, Indiana, Georgia, Missouri, Pennsylvania, Ohio',
    'Platte': 'Wyoming, Missouri, Nebraska',
    'Plymouth': 'Iowa, Massachusetts',
    'Pocahontas': 'Iowa, West Virginia',
    'Polk': 'Iowa, Minnesota, Florida, Arkansas, Georgia, Texas, Tennessee, Wisconsin, North Carolina, Missouri, Nebraska, Oregon',
    'Pontotoc': 'Mississippi, Oklahoma',
    'Pope': 'Minnesota, Arkansas, Illinois',
    'Portage': 'Wisconsin, Ohio',
    'Pottawatomie': 'Kansas, Oklahoma',
    'Potter': 'Texas, Pennsylvania',
    'Pulaski': 'Kentucky, Arkansas, Illinois, Indiana, Georgia, Virginia, Missouri',
    'Putnam': 'Florida, Illinois, Indiana, Georgia, Tennessee, West Virginia, New York, Missouri, Ohio',
    'Quitman': 'Mississippi, Georgia',
    'Ramsey': 'Minnesota, North Dakota',
    'Randolph': 'Alabama, Arkansas, Illinois, Indiana, Georgia, West Virginia, North Carolina, Missouri',
    'Red River': 'Louisiana, Texas',
    'Renville': 'Minnesota, North Dakota',
    'Rice': 'Kansas, Minnesota',
    'Richland': 'Louisiana, Illinois, South Carolina, Wisconsin, Montana, North Dakota, Ohio',
    'Richmond': 'Georgia, Virginia, North Carolina',
    'Ripley': 'Indiana, Missouri',
    'Roane': 'Tennessee, West Virginia',
    'Roberts': 'Texas, South Dakota',
    'Robertson': 'Kentucky, Texas, Tennessee',
    'Rock': 'Minnesota, Wisconsin, Nebraska',
    'Rockingham': 'Virginia, North Carolina, New Hampshire',
    'Roosevelt': 'New Mexico, Montana',
    'Rowan': 'Kentucky, North Carolina',
    'Rush': 'Kansas, Indiana',
    'Rusk': 'Texas, Wisconsin',
    'Russell': 'Kentucky, Alabama, Virginia',
    'Rutherford': 'Tennessee, North Carolina',
    'Sabine': 'Louisiana, Texas',
    'Saline': 'Kansas, Arkansas, Illinois, Missouri, Nebraska',
    'San Juan': 'Colorado, Washington, Utah, New Mexico',
    'San Miguel': 'Colorado, New Mexico',
    'Santa Cruz': 'California, Arizona',
    'Schuyler': 'Illinois, New York, Missouri',
    'Scotland': 'Missouri, North Carolina',
    'Scott': 'Kentucky, Kansas, Iowa, Minnesota, Mississippi, Arkansas, Indiana, Tennessee, Virginia, Missouri',
    'Seminole': 'Florida, Georgia, Oklahoma',
    'Seneca': 'New York, Ohio',
    'Sevier': 'Arkansas, Tennessee, Utah',
    'Seward': 'Kansas, Nebraska',
    'Shelby': 'Kentucky, Iowa, Alabama, Indiana, Illinois, Texas, Tennessee, Missouri, Ohio',
    'Sheridan': 'Kansas, Wyoming, Nebraska, North Dakota',
    'Sherman': 'Kansas, Texas, Nebraska, Oregon',
    'Sierra': 'California, New Mexico',
    'Simpson': 'Kentucky, Mississippi',
    'Sioux': 'Iowa, Nebraska, North Dakota',
    'Smith': 'Kansas, Mississippi, Texas, Tennessee',
    'Somerset': 'Maine, Maryland, New Jersey, Pennsylvania',
    'Spencer': 'Kentucky, Indiana',
    'St. Charles': 'Louisiana, Missouri',
    'St. Clair': 'Michigan, Alabama, Illinois, Missouri',
    'St. Joseph': 'Michigan, Indiana',
    'St. Louis': 'Minnesota, Missouri',
    'Stafford': 'Kansas, Virginia',
    'Stanton': 'Kansas, Nebraska',
    'Stark': 'Illinois, North Dakota, Ohio',
    'Steele': 'Minnesota, North Dakota',
    'Stephens': 'Georgia, Texas, Oklahoma',
    'Steuben': 'Indiana, New York',
    'Stevens': 'Kansas, Minnesota, Washington',
    'Stewart': 'Georgia, Tennessee',
    'Stone': 'Mississippi, Arkansas, Missouri',
    'Suffolk': 'Massachusetts, New York',
    'Sullivan': 'Indiana, Tennessee, New York, New Hampshire, Missouri, Pennsylvania',
    'Summit': 'Colorado, Utah, Ohio',
    'Sumner': 'Kansas, Tennessee',
    'Sumter': 'Florida, Alabama, Georgia, South Carolina',
    'Surry': 'Virginia, North Carolina',
    'Sussex': 'Delaware, Virginia, New Jersey',
    'Talbot': 'Maryland, Georgia',
    'Taylor': 'Kentucky, Iowa, Florida, Georgia, Texas, West Virginia, Wisconsin',
    'Tazewell': 'Illinois, Virginia',
    'Terrell': 'Georgia, Texas',
    'Teton': 'Idaho, Wyoming, Montana',
    'Texas': 'Missouri, Oklahoma',
    'Thomas': 'Kansas, Georgia, Nebraska',
    'Thurston': 'Washington, Nebraska',
    'Tioga': 'New York, Pennsylvania',
    'Tipton': 'Indiana, Tennessee',
    'Todd': 'Kentucky, Minnesota, South Dakota',
    'Trinity': 'California, Texas',
    'Turner': 'Georgia, South Dakota',
    'Tyler': 'Texas, West Virginia',
    'Union': 'Kentucky, Indiana, Iowa, Louisiana, Mississippi, Florida, Arkansas, Illinois, Georgia, South Dakota, South Carolina, Tennessee, New Mexico, New Jersey, Oregon, Pennsylvania, North Carolina, Ohio',
    'Upshur': 'Texas, West Virginia',
    'Valley': 'Idaho, Montana, Nebraska',
    'Van Buren': 'Iowa, Michigan, Arkansas, Tennessee',
    'Vermilion': 'Louisiana, Illinois',
    'Vernon': 'Louisiana, Wisconsin, Missouri',
    'Wabash': 'Indiana, Illinois',
    'Walker': 'Alabama, Georgia, Texas',
    'Walton': 'Florida, Georgia',
    'Walworth': 'South Dakota, Wisconsin',
    'Ward': 'Texas, North Dakota',
    'Warren': 'Kentucky, Indiana, Iowa, Mississippi, Illinois, Georgia, Tennessee, Virginia, New Jersey, New York, Missouri, Pennsylvania, North Carolina, Ohio',
    'Washington': 'Kansas, Kentucky, Indiana, Iowa, Minnesota, Mississippi, Maryland, Louisiana, Maine, Colorado, Alabama, Arkansas, Florida, Idaho, Illinois, Georgia, Tennessee, Wisconsin, Vermont, Texas, Utah, Virginia, New York, Missouri, Nebraska, Oregon, Oklahoma, Rhode Island, Pennsylvania, North Carolina, Ohio',
    'Wayne': 'Kentucky, Indiana, Iowa, Mississippi, Michigan, Illinois, Georgia, Tennessee, West Virginia, New York, Missouri, Nebraska, Pennsylvania, North Carolina, Ohio',
    'Webster': 'Kentucky, Iowa, Mississippi, Louisiana, Georgia, West Virginia, Missouri, Nebraska',
    'Wells': 'Indiana, North Dakota',
    'Westmoreland': 'Virginia, Pennsylvania',
    'Wheeler': 'Georgia, Texas',
    'White': 'Indiana, Arkansas, Illinois, Georgia, Tennessee',
    'Whitley': 'Kentucky, Indiana',
    'Wilcox': 'Alabama, Georgia',
    'Wilkes': 'Georgia, North Carolina',
    'Wilkinson': 'Mississippi, Georgia',
    'Williams': 'North Dakota, Ohio',
    'Williamson': 'Illinois, Tennessee, Texas',
    'Wilson': 'Kansas, Tennessee, Texas, North Carolina',
    'Windham': 'Connecticut, Vermont',
    'Winnebago': 'Iowa, Illinois, Wisconsin',
    'Winston': 'Mississippi, Alabama',
    'Wise': 'Virginia, Texas',
    'Wood': 'West Virginia, Wisconsin, Texas, Ohio',
    'Woodford': 'Kentucky, Illinois',
    'Worcester': 'Massachusetts, Maryland',
    'Worth': 'Iowa, Georgia, Missouri',
    'Wright': 'Iowa, Minnesota, Missouri',
    'Wyoming': 'West Virginia, New York, Pennsylvania',
    'York': 'Maine, South Carolina, Virginia, Nebraska, Pennsylvania',
    'Yuma': 'Colorado, Arizona'
}