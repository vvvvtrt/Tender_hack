import React, {useState} from 'react'
import PropTypes from 'prop-types'
import './header.css'
import Input from '../input/input'
import logo from '../../../public/logo.png';

const Header = () => {

    return(
    <div className="header">
        <img src={logo} style={{"margin-left": "40px"}}/>
        <div>Оставить обращение</div>
        <div>Центр поддержки</div>
        <div>Г. Москва</div>
        <div style={{"margin-right": "40px"}}>Пользователь</div>



        </div>
    
)

}

export default Header;
