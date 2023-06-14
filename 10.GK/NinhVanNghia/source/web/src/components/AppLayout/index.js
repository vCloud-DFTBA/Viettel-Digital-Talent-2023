import React from "react";

import AppHeader from "./AppHeader";
import AppFooter from "./AppFooter";


function AppLayout({children}) {
    return (
        <div className="App vw-100">
            <div className="page-wrapper d-flex flex-column flew-grow-1 min-vh-100">
                <AppHeader/>
                {children}
                <AppFooter/>
            </div>
        </div>
    )
}


export default AppLayout
