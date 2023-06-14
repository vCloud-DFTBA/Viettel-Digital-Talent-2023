import AppFrame from "./AppFrame";
import GlobalStyles from '@mui/material/GlobalStyles';
import { styled } from '@mui/material/styles';
import AppContainer from "./AppContainer";

const Main = styled('main', {
  shouldForwardProp: (prop) => prop !== 'disableToc',
})(({ disableToc, theme }) => ({
  display: 'flex',
  width: '100%',
  ...(disableToc && {
    [theme.breakpoints.up('lg')]: {
      marginRight: '5%',
    },
  }),
  [theme.breakpoints.up('lg')]: {
    width: 'calc(100% - var(--MuiDocs-navDrawer-width))',
  },
}));

const StyledAppContainer = styled(AppContainer, {
  shouldForwardProp: (prop) => prop !== 'disableAd' && prop !== 'disableToc',
})(({ disableAd, disableToc, theme }) => {
  return {
    position: 'relative',
    ...(!disableAd && {
      '&& .description': {
        marginBottom: 198,
      },
      '&& .description.ad': {
        marginBottom: 40,
      },
    }),
    ...(!disableToc && {
      [theme.breakpoints.up('sm')]: {
        width: 'calc(100% - var(--MuiDocs-toc-width))',
      },
      [theme.breakpoints.up('lg')]: {
        paddingLeft: '60px',
        paddingRight: '60px',
      },
    }),
  };
});

export function AppLayout(props) {
  
  const {
    children,
    disableAd = true,
    disableToc = true,
  } = props;

  return (
    <AppFrame>
      <GlobalStyles
        styles={{
          ':root': {
            '--MuiDocs-navDrawer-width': '300px',
            '--MuiDocs-toc-width': '240px',
          },
        }}
      />
      <Main disableToc={disableToc}>
        <StyledAppContainer disableAd={disableAd} disableToc={disableToc}>
          {children}
        </StyledAppContainer>
      </Main>
    </AppFrame>
  );
}