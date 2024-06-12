import React, { memo } from "react";
import styles from "./_attendees.module.scss";
import AttendeesTable from "./AttendeesTable";

function AttendeesDashboard() {
  return (
    <>
      <div className={styles.container}>
        <h1 className={styles.title}>Students Management</h1>
        <div className={styles.table}>
          <AttendeesTable />
        </div>
      </div>
    </>
  );
}

export default memo(AttendeesDashboard);
