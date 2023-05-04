/*==================== SCROLL REVEAL ANIMATION ====================*/
const sr = ScrollReveal({
    distance: '60px',
    duration: 2800,
    // reset: true,
    mobile: false,
})


sr.reveal(`.happy-scoops, 
            .reseller-top, 
            .middle-address,
            .feedbacks-title,
            .feedbacks-button,
            .feedbacks-main,
            .footer-main,
            .header-top,
            .sizes-top,
            .statement,
            .smiley,
            .paragraph-container,
            .tagline-container,
            .gallery-container,
            .ques-container,
            .reach-container,
            .form-container`,{
    origin: 'top',
    interval: 100,
})

sr.reveal(`.best-left, 
            .img-tagline, 
            .icon-address,
            .store-main h1,
            .store-main p,
            .cla,
            .del,
            .btn-view`,{
    origin: 'left',
    // interval: 100,
})

sr.reveal(`.img-main, 
            .tagline-text,  
            .address-store,
            .store-right i,
            .store-right p,
            .store-right h1,
            .spe,
            .ng`,{
    origin: 'right',
})
