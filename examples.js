
            fetch("http://localhost:3002/api/add_users", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    [ add object of key values based on the struct ]
                })
            }).then(response => response.json()).then(data => console.log(data)); 
            

            fetch("http://localhost:3002/api/get_users").then(response => response.json()).then(data => console.log(data));
            

            fetch("http://localhost:3002/api/get_one_usersuser_id").then(response => response.json()).then(data => console.log(data));
            

            fetch("http://localhost:3002/api/get_one_usersemail").then(response => response.json()).then(data => console.log(data));
            

            fetch("http://localhost:3002/api/get_one_usersname").then(response => response.json()).then(data => console.log(data));
            

            fetch("http://localhost:3002/api/get_one_userspassword_hash").then(response => response.json()).then(data => console.log(data));
            

            fetch("http://localhost:3002/api/add_notes", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    [ add object of key values based on the struct ]
                })
            }).then(response => response.json()).then(data => console.log(data)); 
            

            fetch("http://localhost:3002/api/get_notes").then(response => response.json()).then(data => console.log(data));
            

            fetch("http://localhost:3002/api/get_one_notesnote_id").then(response => response.json()).then(data => console.log(data));
            

            fetch("http://localhost:3002/api/get_one_notesuser_id").then(response => response.json()).then(data => console.log(data));
            

            fetch("http://localhost:3002/api/get_one_notestitle").then(response => response.json()).then(data => console.log(data));
            

            fetch("http://localhost:3002/api/get_one_notestext").then(response => response.json()).then(data => console.log(data));
            

            fetch("http://localhost:3002/api/get_one_notescreated_at").then(response => response.json()).then(data => console.log(data));
            

            fetch("http://localhost:3002/api/get_one_noteslabel").then(response => response.json()).then(data => console.log(data));
            

            fetch("http://localhost:3002/api/get_one_notesvector_representation").then(response => response.json()).then(data => console.log(data));
            
