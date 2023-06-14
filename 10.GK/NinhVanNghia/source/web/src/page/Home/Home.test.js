import renderer from 'react-test-renderer';

import Home from '.';
import { attendeeQuery } from 'api/attendeeQuery';


test("It should render", async () => {
    jest.spyOn(attendeeQuery, 'useList').mockResolvedValue(Promise.resolve({}));
    expect(renderer.create(<Home/>).toJSON()).toMatchSnapshot()
})
