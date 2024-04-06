import React from 'react'
import './similar.css'

const Similar = () =>{
    let similarData = [{image: '/', name: 'Object1', discribe: "discribe of object"},
    {image: '/', name: 'Object1', discribe: "discribe of object"},
    {image: '/', name: 'Object1', discribe: "discribe of object"},
    {image: '/', name: 'Object1', discribe: "discribe of object"},
    {image: '/', name: 'Object1', discribe: "discribe of object"},
    {image: '/', name: 'Object1', discribe: "discribe of object"},


]

    const similar = similarData.map((item, index) =>
        <li className="li-similar" key={index}>
            <img src={item.image} className="img-similar"></img>
            <div style={{"text-align": "left"}}>
                <span><b>{item.name}</b></span>
                <p>{item.discribe}</p>
            </div>
            <div className="buttons-similar-cont">
                <button className="button-similar">Подать предложение</button>
                <button className="button-similar">Использовать как шаблон</button>

            </div>
        </li>
    )

    console.log(similar)
    return(
    <ul className='similar-ul'>
     {similar}
    </ul>
    )
} 

export default Similar;