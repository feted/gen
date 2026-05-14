import random, csv
from datetime import datetime

# Male and female first name pools (50+ each)
male_names = [
    "Thabo","Sipho","Themba","Kagiso","Sibusiso","Lethabo","Siyabonga","Bongani","Mandla","Vusi",
    "Andile","Mpho","Kabelo","Lucky","Tshepo","Jabulani","Sandile","Nkosi","Khaya","Ayanda",
    "Lungile","Justice","Lebogang","Oupa","Phumlani","Sizwe","Xolani","Bhekizizwe","Dumisani","Mfundo",
    "Nkosinathi","Mthokozisi","Senzo","Njabulo","Vuyo","Malusi","Zola","Katlego","Tumelo","Siphesihle",
    "Mzwandile","Mlungisi","Samkelo","Siyanda","Thulani","Nhlanhla","Sifiso","Bonginkosi","Mxolisi","Mbuso"
]

female_names = [
    "Nomsa","Lerato","Thandi","Zanele","Nandi","Ayanda","Buhle","Nosipho","Precious","Palesa",
    "Bonisiwe","Khanyi","Lindiwe","Sibongile","Thembi","Nokuthula","Jabulile","Phumzile","Ntombizodwa","Hlengiwe",
    "Nompumelelo","Zodwa","Nonhlanhla","Nomvula","Noxolo","Nthabiseng","Tshepiso","Boitumelo","Keabetswe","Mapule",
    "Refilwe","Kgomotso","Dimakatso","Matshepo","Masego","Lebohang","Motlalepula","Mpho","Dineo","Karabo",
    "Naledi","Omphile","Tsholofelo","Lesego","Kutlwano","Mmabatho","Onkgopotse","Molebogeng","Itumeleng","Gugu"
]

last_names = [
    "Mokoena","Dlamini","Naidoo","Nkosi","Khumalo","Sithole","Zulu","Mthembu","Ndlovu","Mahlangu",
    "Mabuza","Cele","Hlongwane","Shabalala","Gumede","Mkhize","Maseko","Msimango","Baloyi","Maluleke",
    "Ramaphosa","Motsepe","Phakathi","Mofokeng","Radebe","Mabena","Mnguni","Mlambo","Mphahlele","Motsamai",
    "Seabi","Tshabalala","Molefe","Modise","Mokoetle","Mothibi","Mokgosi","Moeketsi","Mothapo","Kgosi",
    "Mothlabi","Mothusi","Mothlatsi","Mothapo","Mothibi","Mothlatsi","Mothusi","Mothapo","Mothibi","Mothlatsi"
]

# Industries and expanded business domains
industries = {
    "Mining":["mininggroup.co.za","capetownmining.co.za","joburgmining.co.za"],
    "Finance":["finconsult.co.za","joburgfinance.co.za","capefinance.co.za"],
    "Retail":["retailhub.co.za","durbanretail.co.za","capetownretail.co.za"],
    "Technology":["techsolutions.co.za","joburgtech.co.za","capetowntech.co.za"],
    "Logistics":["logistics.co.za","durbanlogistics.co.za","joburglogistics.co.za"],
    "Agriculture":["agrifarm.co.za","limpopoagri.co.za","mpumalangafarms.co.za"],
    "Construction":["buildgroup.co.za","joburgconstruction.co.za","capetownconstruction.co.za"],
    "Healthcare":["healthcare.co.za","durbanhealth.co.za","capetownhealth.co.za"],
    "Tourism":["tourism.co.za","capetourism.co.za","durbantravel.co.za"],
    "Education":["educationhub.co.za","joburgedu.co.za","capetownedu.co.za"]
}

company_types = ["Pty Ltd","Close Corporation","Sole Proprietor","Partnership","Trust"]
statuses = ["Active","Closed"]

cities = [
    "Johannesburg, Gauteng","Cape Town, Western Cape","Durban, KwaZulu-Natal",
    "Pretoria, Gauteng","Port Elizabeth, Eastern Cape","Bloemfontein, Free State",
    "Polokwane, Limpopo","Nelspruit, Mpumalanga","Kimberley, Northern Cape",
    "Rustenburg, North West","East London, Eastern Cape","George, Western Cape",
    "Pietermaritzburg, KwaZulu-Natal","Welkom, Free State","Mthatha, Eastern Cape"
]

providers = ["gmail.com","yahoo.com","outlook.com","hotmail.com",
             "telkomsa.net","vodamail.co.za","mtnmail.co.za","webmail.co.za","iafrica.com"]

def random_phone():
    prefix = random.choice(["071","072","073","074","081","082","083","084"])
    number = "".join(str(random.randint(0,9)) for _ in range(7))
    return f"+27 {prefix} {number}"

def random_registration():
    year = random.randint(1990,2025)
    seq = random.randint(100000,999999)
    return f"{year}/{seq}/07"

def realistic_balance():
    base = 2000000
    skew = int(random.lognormvariate(0.5,0.6) * 500000)
    return f"{base + skew:,}"

def realistic_revenue():
    revenue = random.randint(5000000,200000000)
    return f"{revenue:,}"

def random_email(first_name, last_name, industry, company_name=None):
    if company_name and random.random() < 0.4:
        domain = company_name.replace(" ", "").lower() + ".co.za"
    else:
        domain = random.choice(industries.get(industry, providers))
    return f"{first_name.lower()}.{last_name.lower()}{random.randint(1,99)}@{domain}"

def generate_row(owner_id):
    gender = random.choice(["Male","Female"])
    first_name = random.choice(male_names) if gender=="Male" else random.choice(female_names)
    last_name = random.choice(last_names)
    full_name = f"{first_name} {last_name}"
    dob = f"{random.randint(1950,1995)}-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
    phone = random_phone()
    company_name = f"{last_name} {random.choice(['Holdings','Consulting','Logistics','Group','Enterprises'])}"
    industry = random.choice(list(industries.keys()))
    email = random_email(first_name, last_name, industry, company_name)
    company_type = random.choice(company_types)
    address = random.choice(cities)
    reg_number = random_registration()
    revenue = realistic_revenue()
    balance = realistic_balance()
    status = random.choice(statuses)
    return [owner_id, full_name, gender, dob, phone, email,
            company_name, company_type, industry, address,
            reg_number, revenue, balance, status]

header = ["owner_id","full_name","gender","dob","phone_number","email",
          "company_name","company_type","industry","company_address",
          "registration_number","annual_revenue_ZAR","account_balance_ZAR","status"]

with open("sa_business_owners.csv","w",newline="",encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    for i in range(1,1001):
        writer.writerow(generate_row(i))

print("Synthetic SA business owners dataset saved to sa_business_owners.csv")
