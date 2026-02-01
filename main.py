from pyscript import display, document


def intrams_checker(e):
    document.getElementById('output').innerHTML = ' '
    document.getElementById('image').innerHTML = ' '
    
    registration = document.querySelector('input[name="registration"]:checked').value
    clearance = document.querySelector('input[name="clearance"]:checked').value
    section = document.getElementById('section').value

    if registration != 'registered':
        display(f'Not eligible: student is not registered for Intrams. Ask your PE teacher regarding the online registraton.', target='output')
    elif clearance != 'cleared':
        display(f'Not eligible: medical clearance required. Go to the clinic and secure your clearance.', target='output')
   
    elif section == '7 Emerald':
        display(f'Congratulations! You are part of Team Hufflepuff', target='output')
        document.getElementById("image").innerHTML = '<img class="image animate__animated animate__fadeIn animate__duration-8s" src="https://i.pinimg.com/1200x/2d/06/da/2d06da8aad7960490720677694debe51.jpg">'
    elif section == '7 Ruby':
        display(f'Congratulations! You are part of Team Hufflepuff', target='output')
        document.getElementById("image").innerHTML = '<img class="image animate__animated animate__fadeIn animate__duration-8s" src="https://i.pinimg.com/1200x/2d/06/da/2d06da8aad7960490720677694debe51.jpg">'
    
    elif section == '8 Emerald':
        display(f'Congratulations! You are part of Team Gryffindor', target='output')
        document.getElementById("image").innerHTML = '<img class="image animate__animated animate__fadeIn animate__duration-8s" src="https://i.pinimg.com/1200x/c2/0c/3a/c20c3a143e6616f995e098866d19b89b.jpg">' 
    elif section == '8 Ruby':
        display(f'Congratulations! You are part of Team Ravenclaw', target='output')
        document.getElementById("image").innerHTML = '<img class="image animate__animated animate__fadeIn animate__duration-8s" src="https://i.pinimg.com/736x/0d/8e/eb/0d8eeb998302e4f79d97c8bc44909d26.jpg">' 
   
    elif section == '9 Emerald':
        display(f'Congratulations! You are part of Team Slytherin', target='output')
        document.getElementById("image").innerHTML = '<img class="image animate__animated animate__fadeIn animate__duration-8s" src="https://i.pinimg.com/1200x/2d/0b/b1/2d0bb17a064b01e4222b7f05c06150e0.jpg">' 
    elif section == '9 Ruby':
        display(f'Congratulations! You are part of Team Slytherin', target='output')
        document.getElementById("image").innerHTML = '<img class="image animate__animated animate__fadeIn animate__duration-8s" src="https://i.pinimg.com/1200x/2d/0b/b1/2d0bb17a064b01e4222b7f05c06150e0.jpg">' 
    
    elif section == '10 Emerald':
        display(f'Congratulations! You are part of Team Gryffindor', target='output')
        document.getElementById("image").innerHTML = '<img class="image animate__animated animate__fadeIn animate__duration-8s" src="https://i.pinimg.com/1200x/c2/0c/3a/c20c3a143e6616f995e098866d19b89b.jpg">'   
    elif section == '10 Ruby':
        display(f'Congratulations! You are part of Team Ravenclaw', target='output')
        document.getElementById("image").innerHTML = '<img class="image animate__animated animate__fadeIn animate__duration-8s" src="https://i.pinimg.com/736x/0d/8e/eb/0d8eeb998302e4f79d97c8bc44909d26.jpg">' 