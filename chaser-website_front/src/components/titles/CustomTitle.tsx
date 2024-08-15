import React, { ReactNode } from 'react';
import { Typography, styled} from '@mui/material';

interface CustomTitleProps {
  children: ReactNode;
}

const CustomTitle: React.FC<CustomTitleProps> = ({ children }) => {


  const StyledTypography = styled(Typography)(() => ({
    color: '#CECECE',
    fontWeight: 'bold',
    fontSize: '4rem',
    textAlign: 'center',
  }));


  return (
    <StyledTypography variant="h1">
      {children}
    </StyledTypography>
  );
};

export default CustomTitle;