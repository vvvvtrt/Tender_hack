import React, {useState} from 'react'
import PropTypes from 'prop-types'
import './popup.css'


const Popup = (props) => {
    const [isVisible, setVisible] = useState(true)

    function handleClick(e){
        e.stopPropagation();
        setVisible(false)
        
    }

    return(<>
    {isVisible &&
        <div className="wrapper--popup" onClick={(e) => handleClick(e)}>
        <div className="popup">
            <div className="popup--top">
                <h1>{props.notification}</h1>
                <p>{props.notificationText}</p>
            </div>
            <div className="popup--bottom">
            <button className="notification-cancel" onClick={() => handleClick()}>Закрыть</button>
            </div>

        </div>
    </div>
    }
    </>
)

}

export default Popup;

Popup.propTypes = {
    notification: PropTypes.string,
    notificationText: PropTypes.string
};