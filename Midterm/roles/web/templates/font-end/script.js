const updateForm = document.querySelector('.insert-form')
        
        const sexRadio = document.querySelectorAll('.sex-radio')
        updateForm.addEventListener('submit', (e)=>{
            e.preventDefault()

            let sex = ''
            for (let gender of sexRadio){
                if (gender.checked){
                    sex = gender.value
                    break
                }
            }
            const data = {
                'id': document.querySelector('#id').value,
                'name': document.querySelector('#name').value,
                'username': document.querySelector('#username').value,
                'birth': document.querySelector('#birth').value,
                'sex': sex,
                'university': document.querySelector('#university').value,
                'major': document.querySelector('#major').value
            }
            console.log(data)

            fetch("http://localhost:3000/updateStudent", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
                })
            .then(response => response.json())
            .then(data => alert('successfully'))
            .catch(error => console.error(error));
        })