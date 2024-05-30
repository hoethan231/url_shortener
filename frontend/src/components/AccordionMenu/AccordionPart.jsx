import React, { useState } from "react";
import CopyBox from "../CopyBox/CopyBox";
import "./AccordionPart.css"

const AccordionPart = () => {

    const [isOpen, setIsOpen] = useState(false);

    function handleClick() {
        setIsOpen(!isOpen);
    }

    return (
        <div className="wrapper">
            <div className="title" onClick={handleClick}>
                <span>This is the title</span>
                <span><i className={`fa-solid fa-angle-${isOpen ? 'up' : 'down'}`}></i></span>
            </div>
            <div className={`info-${isOpen ? 'open' : 'close'}`}>
                <CopyBox/>
            </div>
        </div>
    );
}

export default AccordionPart;