import { styled } from '@mui/material/styles';
import Box from '@mui/material/Box'

const StyledAppContainer = styled(Box)(({ theme }) => {
  return {
    paddingTop: 'calc(var(--MuiDocs-header-height))',
    fontFamily: 'Arial',
    minWidth: '100%',
    minHeight: '100vh',
  };
});

export default function AppContainer(props) {
  return <StyledAppContainer id="main-content" maxWidth={true} {...props} />;
}
