from faker import Faker
from faker.providers import lorem
import pandas as pd

"""Set up the generator"""
fake = Faker()
Faker.seed(4321)
fake.add_provider(lorem)

providers = range(0, 140)
years = ['2016', '2017', '2018']
clusters = [
    {'Cluster': 'STEM', 'Description': "Specialist institutions covering science, technology, engineering and "
                                       "mathematics (as defined by a very high concentration of academic staff in "
                                       "these disciplines). Often high amounts of excellent research, particularly "
                                       "in bioscience & veterinary and engineering."},
    {'Cluster': 'ARTS', 'Description': "Specialist institutions covering arts, music and drama (as defined by a very "
                                       "high concentration of academic staff in these disciplines). A range of sizes "
                                       "of institutions, although many are relatively small and specialist"},
    {'Cluster': 'E', 'Description': "Large universities with broad discipline portfolio across both STEM and non-STEM "
                                    "generating excellent research across all disciplines. Significant amount of "
                                    "research funded by government bodies/hospitals; 9.5% from industry. Large "
                                    "proportion of part-time undergraduate students. Small postgraduate population "
                                    "dominated by taught postgraduates."},
    {'Cluster': 'M', 'Description': "Smaller universities, often with a teaching focus. Academic activity across "
                                    "disciplines, particularly in other health domains and non-STEM. More research "
                                    "activity funded by government bodies/hospitals; 14.7% from industry."},
    {'Cluster': 'X', 'Description': "Large, high research intensive and broad-discipline universities undertaking "
                                    "a significant amount of excellent research. Much of research funded by UKRI and "
                                    "other government bodies; 8.5% from industry. Discipline portfolio balanced across "
                                    "STEM and non-STEM although less clinical medicine activity. Large proportion of "
                                    "taught postgraduates in student population."},
    {'Cluster': 'J', 'Description': "Mid-sized universities with more of a teaching focus (although research is still"
                                    " in evidence). Academic activity across STEM and non-STEM disciplines including"
                                    " other health, computer sciences, architecture/planning, social sciences and"
                                    " business, humanities, arts and design. Research activity funded largely by"
                                    " government bodies/hospitals; 13.7% from industry."},
    {'Cluster': 'V', 'Description': "Very large, very high research intensive and broad-discipline universities "
                                    "undertaking significant amounts of excellent research. Research funded by range "
                                    "of sources including UKRI, other government bodies and charities; "
                                    "10.2% from industry. Significant activity in clinical medicine and STEM. "
                                    "Student body includes significant numbers of taught and research postgraduates."}
]

""" Perspective metadata """
perspectives = [
    {
        'id': 1,
        'name': 'Research Partnerships',
        'has narrative': False,
        'metrics':
            [
                'Contribution to collaborative research (Cash) as proportion of public funding',
                'Co-authorship with non-academic partners as a proportion of total outputs (data provider TBD)'
            ]
    }
    ,
    {
        'id': 2,
        'name': 'Working with business',
        'has narrative': False,
        'metrics':
        [
            'Innovate UK income (KTP and grant) as proportion of research income (Innovate UK)',
            'HE-BCI contract research income with non-SME business normalised by HEI income',
            'HE-BCI contract research income with SME business normalised by HEI income',
            'HE-BCI Consultancy and facilities income with non -SME business normalised by HEI income',
            'HE-BCI Consultancy and facilities income with SME business normalised by HEI income'
        ]
    },
    {
        'id': 3,
        'name': 'Working with the public and third sector',
        'has narrative': False,
        'metrics':
        [
            'HE-BCI contract research income with the public and third sector normalised by HEI income',
            'HE-BCI Consultancy and facilities income with the public and third sector normalised by HEI income'
        ]},
    {
        'id': 4,
        'name': 'Skills, enterprise and entrepreneurship',
        'has narrative': False,
        'metrics':
        [
            'HE-BCI CPD/CE income normalised by HEI income',
            'HE-BCI CPD/CE learner days delivered normalised by HEI income',
            'HE-BCI Graduate start-ups rate by student FTE'
        ]},
    {
        'id': 5,
        'name': 'Local growth and regeneration',
        'has narrative': True,
        'metrics':
        [
            'Regeneration and development income from all sources normalised by HEI income'
            'Additional narrative/contextual information - optional in year 1'
        ]},
    {
        'id': 6,
        'name': 'IP and Commercialisation',
        'has narrative': False,
        'metrics':
        [
            'Estimated current turnover of all active firms per active spinout',
            'Average external investment per formal spinout',
            'Licensing and other IP income as proportion of research income'
        ]},
    {
        'id': 7,
        'name': 'Public and community engagement',
        'has narrative': True,
        'metrics':
        [
            'Self assessment based metric - optional in year 1'
        ]}
]

all_items = []

for provider in providers:
    provider_name = "University " + str(provider)
    provider_institution_context = provider_name + " lorem ipsum dolor sit amet; consectetur adipiscing elit. Aliquam " \
                                                   "lobortis enim id lacus mollis; at malesuada erat posuere. " \
                                                   "Vestibulum ac consequat urna. Nullam in accumsan purus. Vivamus " \
                                                   "laoreet egestas ligula ut aliquam. Nulla eu tristique metus. " \
                                                   "In luctus magna in dictum auctor. Integer felis orci; consequat ac " \
                                                   "tempus quis; iaculis a ex. Vivamus ut ex at nibh pulvinar gravida. " \
                                                   "Fusce at justo odio. Suspendisse et diam vitae arcu rutrum " \
                                                   "sollicitudin. Nulla facilisi. Ut quis quam nisi. Praesent eu metus " \
                                                   "arcu. Maecenas id euismod eros; vitae euismod libero. Class aptent " \
                                                   "taciti sociosqu ad litora torquent per conubia nostra; per " \
                                                   "inceptos himenaeos. Donec urna massa; eleifend at elementum eu; " \
                                                   "luctus id lorem. Praesent nec dui sollicitudin; posuere odio sit " \
                                                   "amet, elementum enim."
    cluster = fake.random.choice(clusters)
    provider_cluster = cluster['Cluster']
    provider_cluster_description = cluster['Description']
    provider_ukprn = '000' + str(provider)
    for year in years:
        for perspective in perspectives:

            perspective_total = 0
            items = []

            for metric in perspective.get('metrics'):

                rand = fake.random.normalvariate(50, 30)/100
                if rand < 0:
                    rand = 0
                if rand > 1:
                    rand = 1

                narrative = None
                if perspective.get('has narrative'):
                    narrative = fake.text(max_nb_chars=850)

                item = {
                    'Academic Year': year,
                    'Provider Name': provider_name,
                    'Provider UKPRN': provider_ukprn,
                    'Provider Institution Context': provider_institution_context,
                    'Cluster': provider_cluster,
                    'Cluster Description': provider_cluster_description,
                    'Perspective': perspective.get('name'),
                    'Perspective Id': perspective.get('id'),
                    'Has Narrative': perspective.get('has narrative'),
                    'Narrative': narrative,
                    'Metric': metric,
                    'Metric Score': rand
                }
                items.append(item)

            all_items = all_items + items

"""Calculate 3-yr average and decile"""
df = pd.DataFrame(all_items)

df['Metric Scaled'] = df.groupby(['Metric', 'Academic Year'])['Metric Score'] \
    .transform(lambda x: (x-min(x))/(max(x)-min(x)))

df['3 Year Metric Average'] = df.groupby(['Provider UKPRN', 'Metric'])['Metric Scaled'] \
    .transform("mean")

df['3 Year Metric Decile'] = 11 - df.groupby(['Metric'])['3 Year Metric Average'] \
    .transform(
    lambda x: pd.qcut(x, 10, duplicates='drop', labels=False)+1)

df['3 Year Metric Scaled'] = df.groupby(['Metric'])['3 Year Metric Average'] \
    .transform(lambda x: (x-min(x))/(max(x)-min(x)))

df['Perspective Score'] = df.groupby(['Provider UKPRN', 'Perspective', 'Academic Year'])['Metric Scaled']\
    .transform("mean")

df['3 Year Perspective Average'] = df.groupby(['Provider UKPRN', 'Perspective'])['Perspective Score'] \
    .transform("mean")

df['3 Year Perspective Scaled'] = df.groupby(['Perspective'])['3 Year Perspective Average'] \
    .transform(lambda x: (x - min(x)) / (max(x) - min(x)))

df['3 Year Perspective Decile'] = 11 - df.groupby(['Perspective'])['3 Year Perspective Scaled'] \
    .transform(
    lambda x: pd.qcut(x, 10, duplicates='drop', labels=False)+1)

df.to_csv("fake_kef_data.csv", index=False)

