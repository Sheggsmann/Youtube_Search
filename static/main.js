window.onload = function() {
    slideOne()
    slideTwo()
}

let sliderOne = document.querySelector('#slider-1')
let sliderTwo = document.querySelector('#slider-2')
let displayValOne = document.querySelector('#range-1')
let displayValTwo = document.querySelector('#range-2')
let minGap = 150

function slideOne() {
    if (parseInt(sliderTwo.value) - parseInt(sliderOne.value) <= minGap) {
        sliderOne.value = parseInt(sliderTwo.value - minGap)
    }
    displayValOne.textContent = sliderOne.value
}

function slideTwo() {
    if (parseInt(sliderTwo.value) - parseInt(sliderOne.value) <= minGap) {
        sliderTwo.value = parseInt(sliderOne.value) + minGap
    }
    if (parseInt(sliderTwo.value) > 9999) {
        displayValTwo.textContent = '10000+'
        return
    }
    displayValTwo.textContent = sliderTwo.value
}


// GET DATA
let videoInput = document.querySelector('#video-input')
let locationInput = document.querySelector('#location-input')
let searchButton = document.querySelector('#submit-btn')

function getSearchData() {
    search_text = videoInput.value
    min_subscribers = sliderOne.value
    max_subscribers = sliderTwo.value
    return {
        'search': search_text,
        'min': min_subscribers,
        'max': max_subscribers
    }
}


function fetchResults() {
    data = getSearchData()
    console.log(data)
        // fetch('/search', {
        //         method: 'POST',
        //         headers: {
        //             'Content-Type': 'application/json'
        //         },
        //         body: JSON.stringify(data)
        //     })
        //     .then(res => res.json())
        //     .then(data => {
        //         response = data['results']
        //         updateResults
        //     })
    fetch(`/search?keyword={data['search]}`)
        .then(res => res.json())
        .then(data => {
            console.log(data)
        })
}


// searchButton.addEventListener('click', () => {
//     fetchResults()
// })



function cardComponent() {
    return ``
}

function submitForm() {
    let searchField = document.querySelector('#video-input')
    let locationField = document.querySelector('#location-input')
    if (searchField.value.trim() == '') {
        searchField.classList.add('error')
        searchField.setAttribute('placeholder', "Search field can't be empty")
        return
    }
    document.querySelector('form').submit()
}


document.querySelector('#submit-btn').addEventListener('click', () => {
    submitForm()
})