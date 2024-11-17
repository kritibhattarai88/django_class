// let tabcontents = document.getElementsByClassName('tab-content');
// let tablinks = document.getElementsByClassName('tab-links');

// function openlink(arg,event) {
//     for (let tabcontent of tabcontents) {
//         tabcontent.classList.remove("active-tab");
//     }
//     for (let tablink of tablinks) {
//         tablink.classList.remove("active");
//     }
//     document.getElementById(arg).classList.add('active-tab');
//     event.currentTarget.classList.add("active");
    
// }

document.addEventListener("DOMContentLoaded", () => {
    const tabContents = document.querySelectorAll('.tab-content');
    const tabLinks = document.querySelectorAll('.tab-links');

    function openlink(arg, event) {
        // Hide all tab contents and remove "active-tab" class
        tabContents.forEach(tabContent => {
            tabContent.classList.remove('active-tab');
        });

        // Remove "active" class from all tab links
        tabLinks.forEach(tabLink => {
            tabLink.classList.remove('active');
        });

        // Show the selected tab content
        const selectedTab = document.getElementById(arg);
        if (selectedTab) {
            selectedTab.classList.add('active-tab');
        }

        // Add "active" class to the clicked tab link
        if (event && event.currentTarget) {
            event.currentTarget.classList.add('active');
        }
    }

    // Initialize the first tab as active (optional)
    document.querySelector('.tab-content').classList.add('active-tab');
});

