import React, { useState } from "react";
import "./CopyBox.css";

const CopyBox = ({ label, link }) => {
    
    const [clicked, setClicked] = useState(false);
    
    const handleCopy = () => {
        setClicked(true);
        navigator.clipboard.writeText(link);
        setTimeout(() => {
            setClicked(false);
        }, 2000)
    }

    return (
        <div className="container">
            <div className="label">
                {label}
            </div>
            <div className="copy-text">
                <input type="text" className="text" value={link} readOnly/>
                <button onClick={handleCopy}>
                    <i className={clicked ? "fa-solid fa-check" : "fa-regular fa-copy fa-xs"}></i>
                </button>
            </div>
        </div>
    );
};

export default CopyBox;