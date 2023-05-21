import React from 'react';
import renderer from 'react-test-renderer';
import { render, screen } from '@testing-library/react';

import AppLayout from './index.js';


describe("<AppLayout/>", () => {
    test("It should render", () => {
        expect(renderer.create(<AppLayout/>).toJSON()).toMatchSnapshot()
    })

    test("It should render child component", () => {
        render(
            <AppLayout>
                some html
            </AppLayout>
        )
        expect(screen.getByText('some html')).toBeDefined()
    })
})
