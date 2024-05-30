import React, { useState } from "react";
import CopyBox from "../CopyBox/CopyBox";
import "./AccordionPart.css"

const AccordionPart = () => {

    const [isOpen, setIsOpen] = useState(true);

    function handleClick() {
        setIsOpen(!isOpen);
    }

    return (
        <div className="wrapper">
            <div className={`title-${isOpen ? 'open' : 'close'}`} onClick={handleClick}>
                <span>This is the title</span>
                <span><i className={`fa-solid fa-angle-${isOpen ? 'up' : 'down'}`}></i></span>
            </div>
            <div className={`info-${isOpen ? 'open' : 'close'}`}>
                <div className="urls"><CopyBox label={"Long URL:"} link={"youtube.com"}/><CopyBox label={"Short URL:"} link={"meow.com"}/></div>
            </div>
        </div>
    );
}

export default AccordionPart;