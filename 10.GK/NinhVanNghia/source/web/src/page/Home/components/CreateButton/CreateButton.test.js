import renderer from 'react-test-renderer';
import userEvent from '@testing-library/user-event';
import { render, screen } from '@testing-library/react';

import CreateButton from '.';


test("It should render", async () => {
    expect(renderer.create(<CreateButton/>).toJSON()).toMatchSnapshot()
})


test("It should open form", async () => {
    render(<CreateButton/>)

    // Click open form
    await userEvent.click(screen.getByText("Thêm người tham dự"))

    // Wait and check
    await screen.findByTestId('app-modal')
})
