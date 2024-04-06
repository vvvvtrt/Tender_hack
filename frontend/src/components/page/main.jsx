import React, {useState} from 'react'
import PropTypes from 'prop-types'
import './main.css'
import Input from '../input/input'
import Similar from '../similar/similar'



const Main = () => {

    return(
    <div className="main">
        <div className="form--main">
            <div className="windows">
                <h4 className="main-h">Общее</h4>
                <div className="window">
                    <Input/>
                    <Similar/>
                </div>
            </div>
        </div>
        <div className="form--main">
            <button className="send-cte">Отправить заявку на CTE</button>
        </div>
    
    </div>
)

}

export default Main;
