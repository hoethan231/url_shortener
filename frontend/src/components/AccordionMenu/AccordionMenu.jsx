import React from "react";
import AccordionPart from "./AccordionPart";
import "./AccordionMenu.css";

const AccordionMenu = () => {

    return (
        <div className="accordion-wrapper">
            <AccordionPart/>
            <AccordionPart/>
            <AccordionPart/>
        </div>
    );

};

export default AccordionMenu;