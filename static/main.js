window.onload = function() {
    slideOne()
    slideTwo()
}

let sliderOne = document.querySelector('#slider-1')
let sliderTwo = document.querySelector('#slider-2')
let displayValOne = document.querySelector('#range-1')
let displayValTwo = document.querySelector('#range-2')
let minGap = 100

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