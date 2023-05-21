import { Suspense, lazy } from "react";
import { ToastContainer } from "react-toastify";
import { Switch, Route } from "react-router-dom";

import AppLayout from "components/AppLayout";

import "react-toastify/dist/ReactToastify.css";


const Home = lazy(() => import("page/Home"));


function App() {
    return (
        <AppLayout>
            <Suspense fallback={"Loading..."}>
                <Switch>
                    <Route exact path={["/", "/home"]} component={Home}/>
                </Switch>
            </Suspense>

            <ToastContainer
                position="top-right"
                autoClose={3000}
                hideProgressBar={false}
                closeOnClick
                rtl={false}
                pauseOnHover
            />
        </AppLayout>
  );
}


export default App;
