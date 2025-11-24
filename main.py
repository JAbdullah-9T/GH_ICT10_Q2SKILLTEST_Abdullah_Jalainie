# SKILLS TEST
from pyscript import display


glee_details = {
    'Name':'Glee Club',
    'Description':'This is a club designed to improve your singing skills!',
    'Meeting Time':'3:00-4:30', 
    'Location':'Music Room',
    'Club Moderator':'Ms. Loyola',
    'Number of Members':'20-30 members',
    'Category':'Non-Academic'
}   #specifiying dictionaries

dance_details = {
    'Name':'Dance Club',
    'Description':'This is a club designed to improve your dancing skills!',
    'Meeting Time':'3:00-4:30', 
    'Location':'OBMC Gym',
    'Club Moderator':'Sir. Marutani',
    'Number of Members':'20-30 members',
    'Category':'Non-Academic'
}   #specifiying dictionaries

commarts_details = {
    'Name':'Commarts Club',
    'Description':'This is a club designed to improve your speaking skills!',
    'Meeting Time':'3:00-4:30', 
    'Location':'SHS Classrooms',
    'Club Moderator': 'Sir. Loreto',
    'Number of Members':'20-30 members',
    'Category':'Academic'
}   #specifiying dictionaries

CLUBS = {
    'glee': glee_details,
    'dance': dance_details,
    'commarts': commarts_details
}

def show_club(e):
    sel = document.getElementById("club_select")
    key = sel.value
    club = CLUBS[key]
    out = document.getElementById("club_info")

    html = f"""
    <h5>{club['Name']}</h5>
    <p><strong>Description:</strong> {club['Description']}</p>
    <p><strong>Meeting Time:</strong> {club['Meeting Time']}</p>
    <p><strong>Location:</strong> {club['Location']}</p>
    <p><strong>Advisor:</strong> {club['Club Moderator']}</p>
    <p><strong>Category:</strong> {club['Category']}</p>
    """

    out.innerHTML = html