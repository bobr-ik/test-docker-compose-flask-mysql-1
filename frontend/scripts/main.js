async function req(){
    a = await fetch('http://158.160.85.97:5000/api?id=1')
    a = await a.json()
    console.log(a)
    document.getElementById('res').innerHTML = a['site']
    console.log(a['data'])
}
