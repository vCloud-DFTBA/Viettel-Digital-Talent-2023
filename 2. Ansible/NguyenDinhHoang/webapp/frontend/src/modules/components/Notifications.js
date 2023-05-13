import * as React from 'react';
import { styled } from '@mui/material/styles';
import NotificationsNoneRoundedIcon from '@mui/icons-material/NotificationsNoneRounded';
import Tooltip from '@mui/material/Tooltip';
import CircularProgress from '@mui/material/CircularProgress';
import IconButton from '@mui/material/IconButton';
import Badge from '@mui/material/Badge';
import Typography from '@mui/material/Typography';
import Popper from '@mui/material/Popper';
import Grow from '@mui/material/Grow';
import MuiPaper from '@mui/material/Paper';
import ClickAwayListener from '@mui/base/ClickAwayListener';
import MuiList from '@mui/material/List';

const Paper = styled(MuiPaper)({
  transformOrigin: 'top right',
  backgroundImage: 'none',
});
const List = styled(MuiList)(({ theme }) => ({
  width: theme.spacing(40),
  maxHeight: 440,
  overflow: 'auto',
  padding: theme.spacing(1, 0),
}));

const Loading = styled('div')(({ theme }) => ({
  display: 'flex',
  justifyContent: 'center',
  margin: theme.spacing(3, 0),
}));


export default function Notifications() {
  const [open, setOpen] = React.useState(false);
  const [tooltipOpen, setTooltipOpen] = React.useState(false);
  const anchorRef = React.useRef(null)
  const handleToggle = () => {
    setOpen((prevOpen) => !prevOpen);
    setTooltipOpen(false);
  };

  return (
    <React.Fragment>
      <Tooltip
        open={tooltipOpen}
        onOpen={() => {
          setTooltipOpen(!open);
        }}
        onClose={() => {
          setTooltipOpen(false);
        }}
        title={'Notifications'}
        enterDelay={300}
      >
        <IconButton
          color="primary"
          ref={anchorRef}
          aria-controls={open ? 'notifications-popup' : undefined}
          aria-haspopup="true"
          onClick={handleToggle}
          data-ga-event-category="AppBar"
          data-ga-event-action="toggleNotifications"
        >
          <Badge
            color="error"
            badgeContent="1"
          >
            <NotificationsNoneRoundedIcon fontSize="small" />
          </Badge>
        </IconButton>
      </Tooltip>
      <Popper
        id="notifications-popup"
        anchorEl={anchorRef.current}
        open={open}
        placement="bottom-end"
        transition
        disablePortal
        role={undefined}
      >
        {({ TransitionProps }) => (
          <ClickAwayListener
            onClickAway={() => {
              setOpen(false);
            }}
          >
            <Grow in={open}
              {...TransitionProps}
            >
              <Paper
                sx={{
                  mt: 0.5,
                  border: '1px solid',
                  borderColor: (theme) =>
                    theme.palette.mode === 'dark' ? 'primaryDark.700' : 'grey.200',
                  boxShadow: (theme) =>
                    `0px 4px 20px ${theme.palette.mode === 'dark'
                      ? 'rgba(0, 0, 0, 0.5)'
                      : 'rgba(170, 180, 190, 0.3)'
                    }`,
                }}
              >
                <List>
                    <Loading sx={{ flexDirection: 'column', alignItems: 'center', mt: 3 }}>
                      <Typography variant="body2" color="text.secondary" sx={{ mb: 1 }}>
                        No notifications
                      </Typography>
                      <CircularProgress size={32} />
                    </Loading>
                </List>
              </Paper>
            </Grow>
          </ClickAwayListener>
        )}
      </Popper>
    </React.Fragment>
  );
}