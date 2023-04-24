import * as React from 'react';
import PropTypes from 'prop-types';
import Button from '@mui/material/Button';
import { styled, alpha } from '@mui/material/styles';
import List from '@mui/material/List';
import Drawer from '@mui/material/Drawer';
import Menu from '@mui/material/Menu';
import Typography from '@mui/material/Typography';
import SwipeableDrawer from '@mui/material/SwipeableDrawer';
import useMediaQuery from '@mui/material/useMediaQuery';
import Box from '@mui/material/Box';
import { unstable_useEnhancedEffect as useEnhancedEffect } from '@mui/utils';
import ArrowDropDownRoundedIcon from '@mui/icons-material/ArrowDropDownRounded';
import { SideBarData } from '../../libs/sidebar';
import { Link, useLocation } from 'react-router-dom';
import ListItemText from '@mui/material/ListItemText';
import clsx from 'clsx';
import { Divider } from '@mui/material';
import ListItemButton from '@mui/material/ListItemButton';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import IconButton from '@mui/material/IconButton'
import MoreHorizIcon from '@mui/icons-material/MoreHoriz';

const savedScrollTop = {};

function ProductDrawerButton(props) {
  const [anchorEl, setAnchorEl] = React.useState(null);
  const open = Boolean(anchorEl);
  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
  };

  return (
    <React.Fragment>
      <Button
        id="mui-product-selector"
        aria-controls="drawer-open-button"
        aria-haspopup="true"
        aria-expanded={open ? 'true' : undefined}
        onClick={handleClick}
        endIcon={<ArrowDropDownRoundedIcon fontSize="small" sx={{ ml: -0.5 }} />}
        sx={(theme) => ({
          py: 0.1,
          minWidth: 0,
          fontSize: theme.typography.pxToRem(13),
          fontWeight: theme.typography.fontWeightMedium,
          color:
            theme.palette.mode === 'dark' ? theme.palette.primary[300] : theme.palette.primary[600],
          '& svg': {
            ml: -0.6,
            width: 18,
            height: 18,
          },
          '& > span': {
            ml: '4px',
          },
        })}
      >
        {props.productName}
      </Button>
      <Menu
        id="mui-product-menu"
        anchorEl={anchorEl}
        open={open}
        onClose={handleClose}
        MenuListProps={{
          'aria-labelledby': 'mui-product-selector',
        }}
        PaperProps={{
          sx: {
            width: { xs: 340, sm: 'auto' },
          },
        }}
      >
      </Menu>
    </React.Fragment>
  );
}

function PersistScroll(props) {
  const { slot, children, enabled } = props;
  const rootRef = React.useRef();

  useEnhancedEffect(() => {
    const parent = rootRef.current ? rootRef.current.parentElement : null;
    const activeElement = parent.querySelector('.app-drawer-active');

    if (!enabled || !parent || !activeElement || !activeElement.scrollIntoView) {
      return undefined;
    }

    parent.scrollTop = savedScrollTop[slot];

    const activeBox = activeElement.getBoundingClientRect();

    if (activeBox.top < 0 || activeBox.top > window.innerHeight) {
      parent.scrollTop += activeBox.top - 8 - 32;
    }

    return () => {
      savedScrollTop[slot] = parent.scrollTop;
    };
  }, [enabled, slot]);

  return <div ref={rootRef}>{children}</div>;
}

PersistScroll.propTypes = {
  children: PropTypes.node.isRequired,
  enabled: PropTypes.bool.isRequired,
  slot: PropTypes.string.isRequired,
};

const ToolbarDiv = styled('div')(({ theme }) => ({
  padding: theme.spacing(2),
  paddingRight: 0,
  height: '100px',
  display: 'flex',
  flexGrow: 1,
  flexDirection: 'row',
  alignItems: 'center',
  justifyContent: 'space-between',
}));

const StyledDrawer = styled(Drawer)(({ theme }) => ({
  [theme.breakpoints.up('xs')]: {
    display: 'none',
  },
  [theme.breakpoints.up('lg')]: {
    display: 'block',
  },
}));

const AppNavPaperComponent = styled('div')(({ theme }) => {
  return {
    width: 'var(--MuiDocs-navDrawer-width)',
    boxShadow: 'none',
    paddingBottom: theme.spacing(5),
    [theme.breakpoints.up('xs')]: {
      borderRadius: '0px 10px 10px 0px',
    },
    [theme.breakpoints.up('sm')]: {
      borderRadius: '0px',
    },
  };
});

const ProductIdentifier = ({ name, metadata, versionSelector }) => (
  <Box sx={{ flexGrow: 1 }}>
    <Typography
      sx={(theme) => ({
        ml: 1,
        color: theme.palette.grey[600],
        fontSize: theme.typography.pxToRem(11),
        fontWeight: 700,
        textTransform: 'uppercase',
        letterSpacing: '.08rem',
      })}
    >
      {metadata}
    </Typography>
    <Box sx={{ display: 'flex' }}>
      <ProductDrawerButton productName={name} />
      {versionSelector}
    </Box>
  </Box>
);

ProductIdentifier.propTypes = {
  metadata: PropTypes.string,
  name: PropTypes.string,
  versionSelector: PropTypes.element,
};

export const Item = styled(
  function Item({ component: Component = 'div', ...props }) {
    return <Component {...props} />;
  },
)(({ theme, hasIcon, depth, subheader }) => {
  const color = {
    color: theme.palette.text.secondary,
    ...(depth === 0 && {
      color: theme.palette.text.primary,
    }),
    ...(subheader && {
      color: theme.palette.grey[600],
    }),
  };

  return {
    ...theme.typography.body2,
    display: 'flex',
    alignItems: 'center',
    borderRadius: 5,
    outline: 0,
    width: '100%',
    paddingTop: 5,
    paddingBottom: 5,
    justifyContent: 'flex-start',
    fontWeight: theme.typography.fontWeightMedium,
    transition: theme.transitions.create(['color', 'background-color'], {
      duration: theme.transitions.duration.shortest,
    }),
    fontSize: theme.typography.pxToRem(14),
    textDecoration: 'none',
    paddingLeft: 31 + (depth > 1 ? (depth - 1) * 10 : 0),
    ...color,
    ...(subheader && {
      marginTop: theme.spacing(1),
      textTransform: 'uppercase',
      letterSpacing: '.08rem',
      fontWeight: theme.typography.fontWeightBold,
      fontSize: theme.typography.pxToRem(11),
    }),
    ...(hasIcon && {
      paddingLeft: 2,
    }),
    '&.app-drawer-active': {
      color:
        theme.palette.mode === 'dark' ? theme.palette.primary[300] : theme.palette.primary[600],
      backgroundColor:
        theme.palette.mode === 'dark' ? theme.palette.primaryDark[700] : theme.palette.primary[50],
      '&:hover': {
        backgroundColor: alpha(
          theme.palette.primary.main,
          theme.palette.action.selectedOpacity + theme.palette.action.hoverOpacity,
        ),
        '@media (hover: none)': {
          backgroundColor: alpha(theme.palette.primary.main, theme.palette.action.selectedOpacity),
        },
      },
      '&.Mui-focusVisible': {
        backgroundColor: alpha(
          theme.palette.primary.main,
          theme.palette.action.selectedOpacity + theme.palette.action.focusOpacity,
        ),
      },
    },
    '& .MuiChip-root': {
      marginTop: '2px',
    },
    ...(!subheader && {
      '&:hover': {
        color: theme.palette.mode === 'dark' ? '#fff' : theme.palette.common.black,
        backgroundColor:
          theme.palette.mode === 'dark'
            ? alpha(theme.palette.primaryDark[700], 0.4)
            : theme.palette.grey[50],
        '@media (hover: none)': {
          color: color.color,
          backgroundColor: 'transparent',
        },
      },
    }),
    '&.Mui-focusVisible': {
      backgroundColor: theme.palette.action.focus,
    },
    [theme.breakpoints.up('md')]: {
      paddingTop: 3,
      paddingBottom: 3,
    },
    '& .ItemButtonIcon': {
      marginLeft: 'auto !important',
      marginRight: '5px',
      color: theme.palette.primary.main,
    },
    '&:hover .ItemButtonIcon': {
      color: theme.palette.text.primary,
      '@media (hover: none)': {
        color: theme.palette.primary.main,
      },
    },
    height: 32,
  };
});

const iOS = typeof navigator !== 'undefined' && /iPad|iPhone|iPod/.test(navigator.userAgent);


export default function AppNavDrawer(props) {
  const { className, disablePermanent, mobileOpen, onClose, onOpen } = props;
  const mobile = useMediaQuery((theme) => theme.breakpoints.down('lg'));

  let location = useLocation();

  const [openTeams, setOpenTeams] = React.useState(true);

  const handleClickTeams = () => {
    setOpenTeams(!openTeams);
  };


  const drawer = (
    <React.Fragment>
      <ToolbarDiv>
        <Link
          to="/"
          style={{ textDecoration: 'none' }}
        >
          <Box
            onClick={onClose}
            aria-label={'goToHome'}
            sx={{
              pr: '12px',
              marginTop: '15px',
              marginBottom: '15px',
              // borderRight: '1px solid',
              borderColor: (theme) =>
                theme.palette.mode === 'dark'
                  ? alpha(theme.palette.primary[100], 0.08)
                  : theme.palette.grey[200],
            }}
          >
            <Box
              sx={{
                borderRadius: '100%',
                backgroundColor: 'white',
                width: 60,
                height: 60,
              }}
            >
              <img src="https://upload.wikimedia.org/wikipedia/vi/b/bf/Logo_HUET.svg" alt="logo" style={{ width: '60px' }} />
            </Box>
          </Box>
        </Link>
      </ToolbarDiv>
      <List sx={{ my: 0.5 }}>
        {SideBarData.map((item) => (
          <Link
            to={item.href}
            onClick={() => {
              if (mobile) {
                onClose();
              }
            }}
            style={{ textDecoration: 'none' }}
            key={item.title + '-key'}
          >
            <Item
              className={clsx({
                'app-drawer-active': location.pathname === item.href,
              })}
            >
              {item.icon}
              <ListItemText primary={item.title} sx={{ marginLeft: '10px' }} />
            </Item>
          </Link>
        ))}
      </List>
      <Divider
        sx={{
          borderColor: (theme) =>
            theme.palette.mode === 'dark'
              ? alpha(theme.palette.primary[100], 0.08)
              : theme.palette.grey[100],
          margin: '20px 0',
        }}
      />
    </React.Fragment>
  )
  
  return (
    <nav className={className} aria-label={'mainNavigation'}>
      {disablePermanent || mobile ? (
        <SwipeableDrawer
          disableBackdropTransition={!iOS}
          variant="temporary"
          open={mobileOpen}
          onOpen={onOpen}
          onClose={onClose}
          ModalProps={{
            keepMounted: true,
          }}
          PaperProps={{
            className: 'algolia-drawer',
            component: AppNavPaperComponent,
          }}
        >
          <PersistScroll slot="swipeable" enabled={mobileOpen}>
            {drawer}
          </PersistScroll>
        </SwipeableDrawer>
      ) : null}
      {disablePermanent || mobile ? null : (
        <StyledDrawer
          variant="permanent"
          PaperProps={{
            component: AppNavPaperComponent,
          }}
          open
        >
          <PersistScroll slot="side" enabled>
            {drawer}
          </PersistScroll>
        </StyledDrawer>
      )}
    </nav>
  );
}