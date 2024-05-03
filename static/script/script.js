text_area_input = document.getElementById("phrase-input");
text_area_input.value = ""
text_area_output = document.getElementById("phrase-output");
text_area_output.value = ""
button_paraphrase = document.getElementById("paraphrase");


button_paraphrase.addEventListener("click",()=>{
    data ={
        "phrase-input":text_area_input.value
    }
    axios.post('http://127.0.0.1:8000/getPhrase', data)
                .then(response => {
                    text_area_output.value = response.data.value
                    console.log('Response:', response.data);
                })
                .catch(error => {
                    // Handle error
                    console.error('Error:', error.response.data);
                });
})
