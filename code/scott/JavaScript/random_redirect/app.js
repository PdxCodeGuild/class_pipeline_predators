// console.log('working');
const pages = ["https://portland.craigslist.org/favorites?fl=aXRlbXM6NzQzMzY0MTEzMSwxOTI5MTg5LDI1MTg2OTQsMjYyODc2MSwzMTU0MzA0LDQ3NzYxNTYsNTg5Nzg3OCw1OTkxMzkxLDYyODI4NzUsNzI1ODMzMA==",
"https://www.disneyplus.com/series/the-book-of-boba-fett/57TL7zLNu2wf", "https://ridebdr.com/wabdr/", 
"https://github.com/PdxCodeGuild/class_pipeline_predators/blob/master/3%20JavaScript/labs/lab03_random_redirector.md",
"https://docs.djangoproject.com/en/4.0/topics/db/examples/many_to_one/", "https://www.google.com/maps/@45.5453727,-122.1626064,619m/data=!3m1!1e3",
"https://www.ebay.com/sch/i.html?_from=R40&_nkw=aria+xd4&_sacat=0&rt=nc&Size=L&_dcat=177076"];

let x= 0;
const min= 0;
const max= pages.length;
function randoPage() {
    let x= (Math.floor(Math.random() * (max - min) ) + min);
    window.location.assign(pages[x]);
}
