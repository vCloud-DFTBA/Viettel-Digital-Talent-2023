import { createCtx } from "./CreateCtx";
import React from "react";
import InternService from "src/services/intern.service";

interface Intern {
  id: string;
  name: string;
  email: string;
  year_of_birth: string;
  university: string;
}

interface TaskContextType {
  rows: Intern[];
  setRows: React.Dispatch<React.SetStateAction<Intern[]>>;
  addInternOpen: boolean;
  setAddInternOpen: React.Dispatch<React.SetStateAction<boolean>>;
  openDeleteDialog: boolean;
  setOpenDeleteDialog: React.Dispatch<React.SetStateAction<boolean>>;
  selected: readonly string[];
  setSelected: React.Dispatch<React.SetStateAction<readonly string[]>>;
  selectedInternID: string;
  setSelectedInternID: React.Dispatch<React.SetStateAction<string>>;
  openEditDialog: boolean;
  setOpenEditDialog: React.Dispatch<React.SetStateAction<boolean>>;
}


export const [useMyTask, MyTaskProvider] = createCtx<TaskContextType>();


export default function MyTaskContext({
  children,
}: {
  children: React.ReactNode;
}) {

  const [rows, setRows] = React.useState<Intern[]>([]);
  const [addInternOpen, setAddInternOpen] = React.useState(false);
  const [openDeleteDialog, setOpenDeleteDialog] = React.useState(false);
  const [selected, setSelected] = React.useState<readonly string[]>([]);
  const [selectedInternID, setSelectedInternID] = React.useState<string>("");
  const [openEditDialog, setOpenEditDialog] = React.useState(false);


  React.useEffect(() => {
    InternService.GetIntern()
      .then((res) => {
        console.log(res);
        setRows(res);
      })
      .catch((err) => {
        console.log(err);
      });
  }, []);

  return (
    <MyTaskProvider
      value={{
        rows,
        setRows,
        addInternOpen,
        setAddInternOpen,
        openDeleteDialog,
        setOpenDeleteDialog,
        selected,
        setSelected,
        selectedInternID,
        setSelectedInternID,
        openEditDialog,
        setOpenEditDialog,
      }}
    >
      {children}
    </MyTaskProvider>
  );
}
