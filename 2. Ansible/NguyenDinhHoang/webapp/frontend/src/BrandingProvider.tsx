import * as React from 'react';
import { deepmerge } from '@mui/utils';
import { ThemeProvider, useTheme, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { getDesignTokens, getThemedComponents } from './modules/brandingTheme';

interface BrandingProviderProps {
  children: React.ReactNode;
  mode?: 'light' | 'dark';
}

export default function BrandingProvider(props: BrandingProviderProps) {
  const { children, mode: modeProp } = props;
  const upperTheme = useTheme();
  const mode = modeProp || upperTheme.palette.mode;
  const theme = React.useMemo(() => {
    const designTokens = getDesignTokens(mode);
    let newTheme = createTheme(designTokens);
    newTheme = deepmerge(newTheme, getThemedComponents(newTheme));
    return newTheme;
  }, [mode]);
  return (
    <ThemeProvider theme={modeProp ? () => theme : theme}>
      {modeProp ? null : <CssBaseline />}
      {children}
    </ThemeProvider>
  );
}