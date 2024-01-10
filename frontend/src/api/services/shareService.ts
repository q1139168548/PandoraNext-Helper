import apiClient from '../apiClient';

import {Share} from '#/entity';

export enum ShareApi {
  list = '/share/list',
  add = '/share/add',
  search = '/share/search',
  delete = '/share/delete',
  update = '/share/update',
}

const getShareList = () => apiClient.get<Share[]>({ url: ShareApi.list });
const addShare = (data: Share) => apiClient.post({ url: ShareApi.add, data });
const updateShare = (data: Share) => apiClient.post({ url: ShareApi.update, data });
const deleteShare = (data: Share) => apiClient.post({ url: ShareApi.delete, data });
const searchShare = (email?: string,uniqueName?:string ) => apiClient.post({ url: ShareApi.search, data: {
  email,
  uniqueName
}});

export default {
  getShareList,
  addShare,
  updateShare,
  searchShare,
  deleteShare
};
