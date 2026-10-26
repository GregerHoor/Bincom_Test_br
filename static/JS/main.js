const infoCard = document.querySelector('.info-card h3');
const statCard = document.querySelector('.stat-card h2');
const lga = document.querySelector('#lga');
const table = document.querySelector('.table-wrapper tbody');
console.log(infoCard)
console.log(lga)

if (infoCard) {
    lga.addEventListener('change', function(e) {
        const allOptions = this.querySelectorAll('option')
        console.log(allOptions)
        let count = 0;

        allOptions.forEach(f => {
            if (f.selected) {
                console.log(f)
                infoCard.textContent = f.textContent;

                const allPolling = table.querySelectorAll('tr');
                
                allPolling.forEach(p => {
                    if (f.value === p.dataset.id) {
                        count += 1
                        p.style.display = '';
                    } else {
                        p.style.display = 'none';
                    }
                })
                statCard.textContent = count;

            }
        });
    })
}



function showSidebar(element) {
    const menu = document.querySelector('nav.footer');
    const sideBarOn = document.querySelector('.side-bar-on');
    const sideBarOff = document.querySelector('.side-bar-off');

    sideBarOn.style.display = 'none';
    sideBarOff.style.display = 'block';
    menu.style.left = "0";
    
}

function closeSidebar(element) {
    const sideBarOn = document.querySelector('.side-bar-on');
    const sideBarOff = document.querySelector('.side-bar-off');
    const menu = document.querySelector('nav.footer');

    sideBarOn.style.display = 'block';
    sideBarOff.style.display = 'none';
    menu.style.left = "-100%";
}

const form = document.getElementById('results-form');

async function get_lat(){
    return new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(
            position => resolve(position.coords.latitude),
            err => reject(err),
            {
                enableHighAccuracy:false,
                timeout:8000,
                maximumAge:9000,
            }
        );
    });
}


async function get_long(){
    return new Promise((resolve, reject) => {
        navigator.geolocation.getCurrentPosition(
            position => resolve(position.coords.longitude),
            err => reject(err),
            {
                enableHighAccuracy:false,
                timeout:8000,
                maximumAge:9000,
            }
        );
    });
}

if (form) {
    form.addEventListener("submit", async function(e) {
        e.preventDefault();

        const csrf_token = document.querySelector('[name="csrfmiddlewaretoken"]');

        const lga_id = document.querySelector('#new-lga option:checked');
        const party_id = document.querySelector('#new-party option:checked');
        const ward_id = document.querySelector('#new-ward option:checked');
        const unit = document.querySelector('#unit');
        const lat = document.querySelector('#lat');
        const long = document.querySelector('#long');
        const polling_unit_num = document.querySelector('#polling_unit_num');
        const polling_unit_name = document.querySelector('#polling_unit_name');
        const polling_unit_desc = document.querySelector('#polling_unit_desc');
        const entered_by_user = document.querySelector('#new-agent');

        lat.value = await get_lat()
        long.value = await get_long()

        //console.log(lat.value)
        //console.log(long.value)

        const payload = {
            'lga':lga_id.value,
            'party':party_id.value,
            'ward':ward_id.value,
            'unit':unit.value,
            'lat':lat.value,
            'long':long.value,
            'polling_unit_num':polling_unit_num.value,
            'polling_unit_name':polling_unit_name.value,
            'polling_unit_desc':polling_unit_desc.value,
            'entered_by_user':entered_by_user.value,
        }
        
        fetch('/api/create_polling_data/', {
            method: 'POST',
            body: JSON.stringify({
                'payload': payload
            }),
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrf_token.value,
            },
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(data.message);
                this.reset()
            }
        })
        .catch(errors => {
            alert('Something went wrong!');
            console.error(errors);
        })
    });
}


function goToUnit(pk) {
    window.location.href = `/polling_unit/${pk}/`;
}