import React from 'react'
import './input.css'

const Input = () => {

    return(
        <div>
            <form className='input-div'>
                <div className="input--div">
                <label htmlFor="type">Вид продукции</label>
                <input className="input-form" id="type" placeholder=''></input>
                </div>

                <div className="input--div">
                <label htmlFor="name">Наименование</label>
                <input className="input-form" id="name" placeholder=''></input>
                </div>

                <div className="input--div">
                <label htmlFor="model">Модель</label>
                <input className="input-form" id="model" placeholder=''></input>
                </div>

                <div style={{"display": "flex", "flexDirection": "rows"}}>
                    <div>
                    <label htmlFor="model">Каталожный номер производителя</label>
                    <input className="input-form" id="number" placeholder=''></input>
                    </div>
                    <div>
                    <label htmlFor="model">Каталожный номер производителя</label>
                    <input className="input-form" id="number" placeholder=''></input>
                    </div>
                </div>

                <div className="input--div">
                <label htmlFor="units">Единицы измерения</label>
                <input className="input-form" id="units" placeholder=''></input>
                </div>

            </form>

        </div>
    )
}

export default Input;