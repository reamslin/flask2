/** processForm: get data from form and make axios call to our API. */

async function processForm(evt) {
    evt.preventDefault()
    // clear error messages
    $(`#name-err`).html('')
    $(`#email-err`).html('')
    $(`#year-err`).html('')
    $(`#color-err`).html('')
    // get form data
    const name = $('#name').val()
    const email = $('#email').val()
    const birthyear = $('#year').val()
    const color = $('#color').val()

    // send POST
    const resp = await axios.post('/api/get-lucky-num', { name, email, birthyear, color });

    handleResponse(resp);

}

/** handleResponse: deal with response from our lucky-num API. */

function handleResponse(resp) {
    $('#lucky-results').html(resp.data)
    if (resp.data.errors) {
        for (input in resp.data.errors) {
            $(`#${input}-err`).html(resp.data.errors[input][0])
        }
    } else {
        $('#lucky-results').html(`Your lucky number is ${resp.data.num.num}. (${resp.data.num.fact})
        Your birth year (${resp.data.year.year}) fact is ${resp.data.year.fact}`)
    }

}


$("#lucky-form").on("submit", processForm);
