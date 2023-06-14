import { Modal, Button } from "react-bootstrap";


function AppModal({show, setShow, children, formik={}, title}) {
    return (
        <Modal data-testid="app-modal"
            show={show} onHide={() => setShow(false)}
            backdrop={true} keyboard={false}
            size={"lg"}
            centered
        >
            <Header setShow={setShow} title={title}/>
            <Modal.Body>
                {children}
            </Modal.Body>
            <Footer setShow={setShow} formik={formik}/>
        </Modal>
    )
}


export default AppModal


// ------------------------------------------------------------------


function Header({setShow, title}) {
    return (
        <Modal.Header style={{ height: "45px" }}>
            <Modal.Title>{title}</Modal.Title>
            <div
                className="btn btn-xs btn-icon btn-light cursor-pointer"
                onClick={() => setShow(false)}
            >
                X
            </div>
        </Modal.Header>
    )
}


function Footer({setShow, formik}) {
    return (
        <Modal.Footer>
            <div className='w-100 d-flex flex-row justify-content-around'>
                <Button className='font-weight-bold' variant="secondary" onClick={() => setShow(false)}>
                    Hủy bỏ
                </Button>
                <Button className='font-weight-bold' variant="primary" onClick={formik.handleSubmit} disabled={formik.isSubmitting}>
                    Thực hiện
                </Button>
            </div>
        </Modal.Footer>
    )
}