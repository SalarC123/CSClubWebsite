const headers = gsap.utils.toArray(".fade-in")

headers.forEach((header) => {
    gsap.to(header, {
        scrollTrigger: {
            trigger: header,
            start: "top 80%",
        },
        opacity: 1,
        marginTop: 0,
        // duration: 0.5,
    })
})
