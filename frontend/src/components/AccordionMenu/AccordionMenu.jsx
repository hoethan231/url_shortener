import React from "react";
import AccordionPart from "./AccordionPart";
import "./AccordionMenu.css";

const AccordionMenu = ({ links, onUrlDelete }) => {

    return (
        <div className="accordion-wrapper">
            {links.map((link, i) => {
                return (<AccordionPart key={i} link={link} onUrlDelete={onUrlDelete}/>);
            })}
        </div>
    );

};

export default AccordionMenu;